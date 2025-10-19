#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量为 pyefun 包内缺少文档字符串（docstring）的函数/方法添加中文 Google 风格占位注释。

说明
- 仅在函数/方法没有任何 docstring 的情况下插入，不会覆盖已有注释。
- 使用 Google 风格的节标题（Args/Returns/Raises），内容为中文，便于与常用工具兼容。
- 尽量从类型注解中推断参数/返回值类型；若无注解则留空。
- 不修改函数实现逻辑，仅在函数体第一行插入三引号多行字符串。

使用方法
    python tools/add_zh_google_docstrings.py

可选参数
    --dry-run   仅打印将要修改的文件与函数，不实际写入。

实现思路
- 使用 ast 解析 Python 文件，定位缺少 docstring 的函数定义节点。
- 通过 ast 节点上的 lineno 信息确定应插入 docstring 的精确文本位置（在函数体首行之前）。
- 通过读取源代码文本，按行插入缩进对齐的 docstring 内容，保持其它文本（含注释）不变。

注意
- 该脚本是幂等的：已有 docstring 的函数不会重复插入。
- 为尽量安全，不会改写函数签名与主体内容。
"""
from __future__ import annotations

import ast
import argparse
import io
import os
import sys
from typing import Dict, List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG_DIR = os.path.join(ROOT, 'pyefun')


def get_source_segment(src: str, node: Optional[ast.AST]) -> Optional[str]:
    if node is None:
        return None
    try:
        return ast.get_source_segment(src, node)
    except Exception:
        # ast.get_source_segment 在低版本可能不可用，尽量降级处理
        return None


def format_default_value(value_src: Optional[str]) -> Optional[str]:
    if not value_src:
        return None
    # 去掉多余空白并规范显示
    val = value_src.strip()
    # 简化: 超长默认值不展开
    if len(val) > 60:
        val = val[:57] + '...'
    return val


def build_param_specs(func: ast.FunctionDef, src: str) -> List[Tuple[str, Optional[str], Optional[str]]]:
    """
    解析函数参数，返回 (name, annotation_str, default_str) 列表。
    不包含 self / cls。
    """
    specs: List[Tuple[str, Optional[str], Optional[str]]] = []
    a = func.args

    # 位置参数（含仅限位置参数）
    pos_args = list(getattr(a, 'posonlyargs', [])) + list(a.args)

    # 为位置参数准备默认值对齐（最后 len(defaults) 个参数有默认值）
    num_defaults = len(a.defaults)
    defaults_map: Dict[str, Optional[str]] = {}
    if num_defaults:
        for arg_node, default_node in zip(pos_args[-num_defaults:], a.defaults):
            defaults_map[arg_node.arg] = format_default_value(get_source_segment(src, default_node))

    # 关键字专用参数
    kw_defaults_map: Dict[str, Optional[str]] = {}
    if a.kwonlyargs:
        for kwarg_node, default_node in zip(a.kwonlyargs, a.kw_defaults):
            kw_defaults_map[kwarg_node.arg] = format_default_value(get_source_segment(src, default_node)) if default_node is not None else None

    def add_arg(arg_node: ast.arg, default_s: Optional[str]):
        name = arg_node.arg
        if name in {"self", "cls"}:
            return
        ann = get_source_segment(src, arg_node.annotation)
        specs.append((name, ann, default_s))

    # 添加位置参数
    for arg_node in pos_args:
        add_arg(arg_node, defaults_map.get(arg_node.arg))

    # *args
    if a.vararg is not None:
        specs.append((f"*{a.vararg.arg}", get_source_segment(src, a.vararg.annotation), None))

    # 仅关键字参数
    for kwarg_node in a.kwonlyargs:
        add_arg(kwarg_node, kw_defaults_map.get(kwarg_node.arg))

    # **kwargs
    if a.kwarg is not None:
        specs.append((f"**{a.kwarg.arg}", get_source_segment(src, a.kwarg.annotation), None))

    return specs


def guess_return_annotation(func: ast.FunctionDef, src: str) -> Optional[str]:
    return get_source_segment(src, func.returns)


def make_google_docstring_zh(func: ast.FunctionDef, src: str) -> str:
    """
    生成中文 Google 风格占位 docstring。
    """
    name = func.name
    params = build_param_specs(func, src)
    ret_ann = guess_return_annotation(func, src)

    lines: List[str] = []
    lines.append('"""')
    # 简要说明
    lines.append(f"{name} 的功能说明（请补充）。")
    lines.append("")

    # 参数
    if params:
        lines.append("Args:")
        for p_name, p_ann, p_def in params:
            # 统一中文描述，占位说明
            if p_ann and p_def is not None:
                lines.append(f"    {p_name} ({p_ann}, 可选): 参数说明。默认值为 {p_def}。")
            elif p_ann:
                lines.append(f"    {p_name} ({p_ann}): 参数说明。")
            elif p_def is not None:
                lines.append(f"    {p_name} (可选): 参数说明。默认值为 {p_def}。")
            else:
                lines.append(f"    {p_name}: 参数说明。")
        lines.append("")

    # 返回值
    if ret_ann:
        lines.append("Returns:")
        lines.append(f"    {ret_ann}: 返回值说明。")
        lines.append("")

    # 结束三引号
    lines.append('"""')

    return "\n".join(lines)


def insert_docstring_into_source(src: str, func: ast.FunctionDef, doc: str) -> str:
    """
    在源文本中为指定函数插入 docstring（作为函数体第一条语句）。
    使用 func.body[0].lineno 定位插入点，并对齐缩进。
    """
    lines = src.splitlines(True)  # 保留换行
    if not func.body:
        # 理论上不会出现，没有 body 的函数非法，这里降级在 def 行之后插入
        insert_line = func.lineno
        indent = ' ' * (func.col_offset + 4)
    else:
        first_stmt = func.body[0]
        insert_line = getattr(first_stmt, 'lineno', func.lineno + 1) - 1  # 转为 0-based 索引
        # 从第一条语句的实际文本前导空白中获取缩进
        # 若获取失败，则用函数缩进+4 空格
        raw_line = lines[insert_line] if 0 <= insert_line < len(lines) else ''
        indent = raw_line[:len(raw_line) - len(raw_line.lstrip('\t '))]
        if not indent:
            indent = ' ' * (func.col_offset + 4)

    # 按缩进包裹 docstring
    doc_indented = "\n".join((indent + ln if ln else ln) for ln in doc.splitlines())
    doc_indented += "\n"

    # 在插入点前插入 docstring 文本
    lines.insert(insert_line, doc_indented)
    return "".join(lines)


def process_file(path: str, dry_run: bool = False) -> Tuple[int, int]:
    """
    处理单个文件。
    返回 (总函数数, 新增 docstring 数)。
    """
    with io.open(path, 'r', encoding='utf-8') as f:
        src = f.read()

    try:
        tree = ast.parse(src)
    except SyntaxError:
        # 跳过无法解析的文件
        return 0, 0

    total_funcs = 0
    to_insert: List[Tuple[ast.FunctionDef, str]] = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            total_funcs += 1
            # 已有 docstring 则跳过
            if ast.get_docstring(node) is not None:
                continue
            # 生成占位文档
            doc = make_google_docstring_zh(node, src)
            to_insert.append((node, doc))

    if not to_insert:
        return total_funcs, 0

    # 为避免行号失效，按函数体起始行从后往前插入
    to_insert.sort(key=lambda item: (item[0].lineno, item[0].col_offset), reverse=True)

    new_src = src
    for func, doc in to_insert:
        new_src = insert_docstring_into_source(new_src, func, doc)

    if not dry_run:
        with io.open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(new_src)

    return total_funcs, len(to_insert)


def iter_python_files(root: str) -> List[str]:
    files: List[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        # 排除 __pycache__
        dirnames[:] = [d for d in dirnames if d != '__pycache__']
        for fn in filenames:
            if fn.endswith('.py'):
                files.append(os.path.join(dirpath, fn))
    return files


def main():
    parser = argparse.ArgumentParser(description='为 pyefun 内缺少 docstring 的函数插入中文 Google 风格注释')
    parser.add_argument('--dry-run', action='store_true', help='仅打印统计信息，不写入文件')
    parser.add_argument('--path', default=PKG_DIR, help='要处理的目录（默认 pyefun）')
    args = parser.parse_args()

    root = os.path.abspath(args.path)
    if not os.path.isdir(root):
        print(f"目录不存在: {root}", file=sys.stderr)
        return 2

    py_files = iter_python_files(root)
    total_files = 0
    total_funcs = 0
    total_added = 0

    for fpath in py_files:
        total_files += 1
        funcs, added = process_file(fpath, dry_run=args.dry_run)
        total_funcs += funcs
        total_added += added
        if added:
            print(f"[DOC] {fpath}: +{added} 个函数注释")

    print(f"完成。文件: {total_files}，函数: {total_funcs}，新增注释: {total_added}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
