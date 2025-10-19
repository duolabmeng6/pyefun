#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
移除由批量工具生成的占位 docstring（包含“的功能说明（请补充）”字样）。

- 仅删除占位注释，不会影响已有的正式注释。
- 通过 AST 精确定位函数体首个语句为字符串常量的 docstring，并在源码层面删除对应文本行。

使用
    python tools/cleanup_placeholder_docstrings.py --path pyefun
    python tools/cleanup_placeholder_docstrings.py --dry-run
"""
from __future__ import annotations

import argparse
import ast
import io
import os
import sys
from typing import List, Tuple

PLACEHOLDER_KEYWORD = "的功能说明（请补充）"


def find_placeholder_doc_ranges(src: str) -> List[Tuple[int, int]]:
    """
    返回需要删除的占位 docstring 的行区间列表（含首尾，0-based）。
    """
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []

    lines = src.splitlines(True)

    ranges: List[Tuple[int, int]] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not node.body:
                continue
            first = node.body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, (ast.Str, ast.Constant)):
                # 兼容 py3.8+ ast.Constant
                try:
                    val = first.value.s if isinstance(first.value, ast.Str) else (first.value.value if isinstance(first.value, ast.Constant) else None)
                except Exception:
                    val = None
                if not isinstance(val, str):
                    continue
                if PLACEHOLDER_KEYWORD not in val:
                    continue
                # 估算 docstring 的行区间
                start = (getattr(first, 'lineno', 1) - 1)
                end = getattr(first, 'end_lineno', None)
                if end is None:
                    # 回退：从 start 开始，找到下一个出现三引号的行
                    # 我们的占位都是用三引号双引号
                    quote_count = 0
                    i = start
                    while i < len(lines):
                        if '"""' in lines[i]:
                            quote_count += lines[i].count('"""')
                        if quote_count >= 2:
                            break
                        i += 1
                    end = i + 1  # 变为非包含式索引时使用
                    ranges.append((start, end - 1))
                else:
                    ranges.append((start, end - 1))
    # 去重并按行号逆序，避免删除造成位移
    ranges = sorted(set(ranges), key=lambda r: (r[0], r[1]), reverse=True)
    return ranges


def remove_ranges_from_source(src: str, ranges: List[Tuple[int, int]]) -> str:
    if not ranges:
        return src
    lines = src.splitlines(True)
    for start, end in ranges:
        # 删除 [start, end] 区间的行
        del lines[start:end + 1]
    return "".join(lines)


def process_file(path: str, dry_run: bool = False) -> Tuple[int, int]:
    with io.open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    ranges = find_placeholder_doc_ranges(src)
    if not ranges:
        return 0, 0
    new_src = remove_ranges_from_source(src, ranges)
    if not dry_run:
        with io.open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(new_src)
    return 1, len(ranges)


def iter_python_files(root: str) -> List[str]:
    files: List[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != '__pycache__']
        for fn in filenames:
            if fn.endswith('.py'):
                files.append(os.path.join(dirpath, fn))
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--path', default=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pyefun'))
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    root = os.path.abspath(args.path)
    if not os.path.isdir(root):
        print(f"目录不存在: {root}", file=sys.stderr)
        return 2

    py_files = iter_python_files(root)
    touched = 0
    removed = 0
    for fp in py_files:
        t, r = process_file(fp, dry_run=args.dry_run)
        touched += t
        removed += r
        if r:
            print(f"[CLEAN] {fp}: 移除 {r} 个占位注释")
    print(f"完成。处理文件: {touched}，移除占位注释: {removed}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
