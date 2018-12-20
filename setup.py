#!/usr/bin/env python3
#coding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals
from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(name="qrcode",
    version="0.0.0",
    author='kazukazuprogram',
    author_email="dbycvil8yiyf7xnlxvh7@yahoo.co.jp",
    maintainer='kazukazuprogram',
    maintainer_email="dbycvil8yiyf7xnlxvh7@yahoo.co.jp",
    description="Generate QR Code.",
    long_description=readme,
    url="https://github.com/kazukazuprogram/qrgen",
    packages=find_packages(),
    license="MIT",
    entry_points={
        'console_scripts':[
                'qrgen = qrcode.__init__',
        ],
    }
)
