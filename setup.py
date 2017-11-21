#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from io import open
from os.path import dirname, join

from setuptools import setup

from setuptools import setup, find_packages


def read(*args):
    return open(join(dirname(__file__), *args), encoding='utf-8').read()

version = read('version.py').strip()

readme = open('README.rst').read()
history = open('CHANGELOG.rst').read().replace('.. :changelog:', '')

install_requires = [
    'markdown2',
    'xhtml2pdf'
]

classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
"""


setup(
    name='markdown2pdf',
    version=version,
    description="""Convert Markdown markup text to a PDF file.""",
    long_description=readme + '\n\n' + history,
    author='Christopher Arndt',
    author_email='info@chrisarndt.de',
    url='https://github.com/SpotlightKid/markdown2pdf',
    include_package_data=True,
    py_modules=['markdown2pdf'],
    install_requires=install_requires,
    license="MIT",
    keywords='markdown,PDF,converter,markup',
    classifiers=[c for c in (c.strip() for c in classifiers.splitlines())
                 if c and not c.startswith('#')],
    entry_points={
        'console_scripts': [
            'markdown2pdf = markdown2pdf:main',
        ]
    },
    zip_safe=False
)
