#!/usr/bin/env python
from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='PyCryptsy',
    version='0.1',
    description='Python binding to the Cryptsy API',
    long_description=read('README.md'),
    url='https://github.com/salfter/PyCryptsy',
    py_modules=['PyCryptsy'],
    zip_safe=False,
    install_requires=["pycurl"],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
)
