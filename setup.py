#!/usr/bin/env python3

from os.path import join, dirname
from setuptools import setup, find_packages

from sudoku.config import VERSION


REQUIRED_PYTHON = (3, 6)


def readme():
    with open(join(dirname(__file__), 'README.md')) as f:
        return f.read()


setup(
    name='sudoku',
    version=VERSION,
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    description='A sudoku solver.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Raymond L. Rivera',
    author_email='ray.l.rivera@gmail.com',
    maintainer='Raymond L. Rivera',
    maintainer_email='ray.l.rivera@gmail.com',
    url='https://gitlab.com/ghost-in-the-zsh/sudoku',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sudoku-solver=sudoku.entrypoints:main'
        ],
    },
    include_package_data=True,
    keywords='sudoku solver backtracking algorithm',
    classifiers=(
        # https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 Only',
        'Topic :: Utilities',
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Games/Entertainment :: Puzzle Games'
    ),
)
