#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path
# Added to fix error.
# See http://stackoverflow.com/questions/9352656/python-assertionerror-when-running-nose-tests-with-coverage  # NOQA
from multiprocessing import util  # NOQA

# Get the long description from DESCRIPTION.rst
with open(path.join(path.abspath(path.dirname(__file__)),
          'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

tests_require = [
    'nose == 1.3.4',
    'coverage == 4.0.3'
]

setup(
    name='gwlf-e',
    version='0.6.1',
    description='A Python port of Generalized Watersheds Loading Functions - Enhanced (MapShed)',
    long_description=long_description,
    url='https://github.com/WikiWatershed/gwlf-e',
    author='Azavea Inc.',
    author_email='systems@azavea.com',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='gwlf-e watershed hydrology',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy == 1.11.0'
    ],
    extras_require={
        'dev': [],
        'test': tests_require,
    },
    test_suite='nose.collector',
    tests_require=tests_require,
)
