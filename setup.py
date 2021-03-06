# -*- coding: utf-8 -*-
#!/bin/env python3

# Copyright (C) 2018 Gaby Launay

# Author: Gaby Launay  <gaby.launay@tutanota.com>
# URL: https://github.com/galaunay/BiblioNetwork
# Version: 0.1

# This file is part of BiblioNetwork

# BiblioNetwork is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from setuptools import setup, find_packages

setup(
    name='BiblioNetwork',
    version='0.1',
    description='Make graphs from bibliography database.',
    author='Gaby Launay',
    author_email='gaby.launay@tutanota.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='bibliography graph',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'samples']),
    install_requires=['numpy', 'pandas', 'matplotlib', 'graph_tool'],
    extras_require={},
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest'],
)
