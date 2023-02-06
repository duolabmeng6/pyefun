# -*- coding: utf-8 -*-
import os

# from github import Github

def 查看系统所有环境变量():
    from icecream import ic
    # 打印系统所有的环境变量
    for item in os.environ:
        name = item
        value = os.environ[item]
        ic(name, value)
# 查看系统所有环境变量()

def 版本号格式加一(版本号):
    版本号 = 版本号.split('.')
    版本号[-1] = str(int(版本号[-1]) + 1)
    版本号 = '.'.join(版本号)
    return 版本号
def 版本号从大小写排序(tags):
    # 删除非数字的版本号
    tags = [tag for tag in tags if tag.replace('.', '').isdigit()]
    tags_dict = []
    for tag in tags:
        # 获取数值
        tag_value = int("".join(tag.split('.')))
        # 长度不足补齐
        tag_value = tag_value * (10 ** (10 - len(str(tag_value))))

        tags_dict.append({
            "tag": tag,
            'tagint': tag_value
        })
    tags_dict.sort(key=lambda student: student['tagint'])
    tags_dict.reverse()
    # 重新组装
    tags = []
    for tag in tags_dict:
        tags.append(tag['tag'])
    return tags

def main():
    GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')
    INPUT_TOKEN = os.environ.get('GITHUB_TOKEN')
    # GITHUB_REPOSITORY = 'duolabmeng6/pyefun'
    g = Github(INPUT_TOKEN)
    repo = g.get_repo(GITHUB_REPOSITORY)
    print("tags number", repo.get_tags().totalCount)
    if repo.get_tags().totalCount == 0:
        # 没有标签的话 创建标签 0.0.1
        sha = repo.get_commits()[0].sha
        新版本号 = "0.0.1"
        repo.create_git_ref(f"refs/tags/{新版本号}", sha)
        return 新版本号
    # 版本号对比
    tags = []
    k = 0
    for tag in repo.get_tags():
        print(tag.name)
        tags.append(tag.name)
        k += 1
        if k == 5:
            break  # 取前5个标签
    print("raw tags", tags)
    # 版本号排序
    tags = 版本号从大小写排序(tags)
    # print("版本号排序:", tags)
    新版本号 = 版本号格式加一(tags[0])
    # print("新版本号:", 新版本号)
    print("new tags", 新版本号)
    sha = repo.get_commits()[0].sha
    print("sha", sha)
    #repo.create_git_ref(f"refs/tags/{新版本号}", sha)
    run = []
    run.append(f'git config user.name github-actions')
    run.append(f'git config user.email github-actions@github.com')
    run.append(f'git tag -fa {新版本号} -m {新版本号}')
    run.append(f'git push --tags -f')
    # 运行命令
    for cmd in run:
        print(cmd)
        os.system(cmd)

    # 替换文本内容 __version__ = '1.2.5'
    # 打开文件 pyefun/__init__.py
    
    with open("pyefun/__init__.py", "r") as f:
        lines = f.readlines()
        # 找到版本号的行
        for i, line in enumerate(lines):
            if '__version__' in line:
                # 找到版本号的行
                version_line = i
                break
        # 替换版本号
        lines[version_line] = f"__version__ = '{新版本号}'\n"

    # 写出文件
    with open("pyefun/__init__.py", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
    # print(版本号从大小写排序(['1.3.2', '1.3.1', '1.2.22', '1.2.21', '1.2.20']))

    exit(0)
