#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path
# Added to fix error.
# See http://stackoverflow.com/questions/9352656/python-assertionerror-when-running-nose-tests-with-coverage  # NOQA
from multiprocessing import util  # NOQA
from gwlfe.AdjUrbanQTotal_2_inner import cc as adjcc  # TODO: use full length names
from gwlfe.AMC5_yesterday_inner import cc as amc5ycc
from gwlfe.CNum_inner import cc as cncc
from gwlfe.CNumImperv_2_inner import cc as cnicc
from gwlfe.CNumPerv_2_inner import cc as cnpcc
from gwlfe.DeepSeep_inner import cc as dscc
from gwlfe.InitSnow_inner import cc as iscc
from gwlfe.InitSnowYesterday_inner import cc as isycc
from gwlfe.Percolation_inner import cc as pcc
from gwlfe.UnsatStor_inner import cc as usscc

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
    version='0.6.2',
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
    # install_requires=[
    #     'numpy == 1.14.2'
    # ],
    extras_require={
        'dev': [],
        'test': tests_require,
    },
    test_suite='nose.collector',
    tests_require=tests_require,
    ext_modules=[adjcc.distutils_extension(), amc5ycc.distutils_extension(), cncc.distutils_extension(),
                 cnicc.distutils_extension(), cnpcc.distutils_extension(), dscc.distutils_extension(),
                 iscc.distutils_extension(), isycc.distutils_extension(), pcc.distutils_extension(),
                 usscc.distutils_extension()]
)
