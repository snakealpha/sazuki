#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'sazuki',
    version = '0.0.1',
    keywords = ('sazuki', 'excel'),
    description = 'A tool to serialize excel file to a file.',
    license = 'MIT License',

    url = 'https://github.com/snakealpha/sazuki',
    author = 'Snake Liu',
    author_email = 'elecelf@outlook.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)