#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-splunk',
    version='0.1.0',
    author='Mark Shao',
    author_email='marksyl1986@gmail.com',
    maintainer='Mark Shao',
    maintainer_email='marksyl1986@gmail.com',
    license='Apache Software License 2.0',
    url='https://github.com/markshao/pytest-splunk',
    description='A simple plugin to use with Pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_pysplunk'],
    install_requires=['pytest>=2.8.1', "requests>=2.9.1"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'splunk = pytest_pysplunk',
        ],
    },
)
