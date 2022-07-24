# -*- coding: utf-8 -*-
import os


def view_all_environment_variables():
    from icecream import ic
    for item in os.environ:
        name = item
        value = os.environ[item]
        ic(name, value)


# view_all_environment_variables()

tagName = os.environ.get('GITHUB_REF_NAME')
print("tagName:", tagName)
fileDir = os.path.dirname(__file__)
print("file dir:", fileDir)
versionFilePath = os.path.join(fileDir, "version.py")
print(f"edit file {versionFilePath} output: version = {tagName}")
# with open(versionFilePath, 'w') as f:
#     f.write(f'version = "{tagName}"')

with open("pyefun/__init__.py", "r") as f:
    lines = f.readlines()
    # 找到版本号的行
    for i, line in enumerate(lines):
        if '__version__' in line:
            # 找到版本号的行
            version_line = i
            break
    # 替换版本号
    lines[version_line] = f"__version__ = '{tagName}'\n"

# 写出文件
with open("pyefun/__init__.py", "w") as f:
    f.writelines(lines)



exit()
