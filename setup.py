# -*- coding: utf-8 -*-

from setuptools import setup
from os import path
import re

package_name = "dtwain"

root_dir = path.abspath(path.dirname(__file__))

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert version
assert license
assert author
assert author_email
assert url

long_description = "The python wrapper for Dynarithmic TWAIN Library Version 5.x"


setup(
    name=package_name,

    version=version,

    license=license,

    author=author,
    author_email=author_email,

    packages=[package_name, path.join(package_name, "__pyinstaller")],
    include_package_data=True,

    url=url,

    description='python-dtwain',
    long_description=long_description,
)