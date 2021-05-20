from distutils.core import setup

# setup(name="pyefun", version="1.0", description="pyefun 为python提供强大且易用的中文函数库，完整的封装了易语言核心支持库所有功能，以及易语言中简单易用的函数",
#       author="duolabmeng(1715109585@qq.com)",
#       py_modules=['core', 'coreUtil'])

def parse_description():
      """
      Parse the description in the README file
      CommandLine:
          pandoc --from=markdown --to=rst --output=README.rst README.md
          python -c "import setup; print(setup.parse_description())"
      """
      from os.path import dirname, join, exists
      readme_fpath = join(dirname(__file__), 'README.rst')
      # This breaks on pip install, so check that it exists.
      if exists(readme_fpath):
            with open(readme_fpath, 'r',encoding="utf-8") as f:
                  text = f.read()
            return text
      return ''

from setuptools import setup, find_packages
setup(
      name = "pyefun",
      version = "1.0.9",
      packages=find_packages('.'),
      # scripts = ['say_hello.py'],
      # Project uses reStructuredText, so ensure that the docutils get
      # installed or upgraded on the target machine
      # install_requires = ['docutils>=0.3'],
      package_data = {
            '': ['*.txt', '*.rst', '*.md'],
      },
      # metadata for upload to PyPI
      author = "duolabmeng",
      author_email = "1715109585@qq.com",
      description = "pyefun 为python提供强大且易用的中文函数库，完整的封装了易语言核心支持库所有功能，以及易语言中简单易用的函数",
      license = "Apache 2",
      keywords = "pyefun 易语言",
      url = "https://github.com/duolabmeng6/pyefun",   # project home page, if any

      long_description=parse_description(),
      long_description_content_type='text/markdown',
)
