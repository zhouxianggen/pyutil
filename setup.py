#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pyutil',
        version = '1.0',
        install_requires = ['psutil'], 
        description = 'python utils',
        url = 'https://github.com/zhouxianggen/pyutil', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['pyutil'],
        data_files = [ ],  
        entry_points = { }   
        )
