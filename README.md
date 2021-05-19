# pyefun

为python提供强大且易用的中文函数库，完整的封装了易语言核心支持库所有功能，以及易语言中简单易用的函数

# 特性

- 完全兼容window linux mac运行
- 完全兼容python运行环境
- 全中文函数名和注释
- 封装了超100+命令
- 全部命令经过测试 100% 测试 放心使用
- 所有命令均有测试用例可以查看后立即使用
- 封装了超丰富的文本处理函数,简单,易用

# 安装

```
pip install pyefun
```


# 笔记

```

打包
python setup.py bdist_wheel

安装
pip install ./dist/pyefun-1.0-py3-none-any.whl --force-reinstall
```

应用开发过程中会频繁变更，每次安装都需要先卸载旧版本很麻烦。使用 develop 开发模式安装的话，实际代码不会拷贝到 site-packages 下，而是除一个指向当前应用的链接（*.egg-link）。这样当前位置的源码改动就会马上反映到 site-packages。使用如下

```
pip install -e .  

或者 

python setup.py develop

twine upload --repository testpypi dist/*
```

# 上传包
注册pypi账号 pypi.python.org

https://packaging.python.org/tutorials/packaging-projects/

```
pip install twine

twine upload dist/*
```
# 打包加发布

```
python setup.py bdist_wheel
twine upload dist/*
```

```

python setup.py bdist_wheel

twine upload --repository testpypi dist/*

```
