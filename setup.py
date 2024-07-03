#!/usr/bin/env python

from codecs import open
from os import path

from setuptools import setup, find_packages

from gwlfe.Input.WaterBudget.AMC5_yesterday_inner import cc as amc5ycc
# Added to fix error.
# See http://stackoverflow.com/questions/9352656/python-assertionerror-when-running-nose-tests-with-coverage  # NOQA
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal_inner import cc as adjcc  # TODO: use full length names
from gwlfe.MultiUse_Fxns.Runoff.CNumImperv_inner import cc as cnicc
from gwlfe.MultiUse_Fxns.Runoff.CNumPerv_inner import cc as cnpcc
from gwlfe.MultiUse_Fxns.Runoff.CNum_inner import cc as cncc
from gwlfe.Input.WaterBudget.DeepSeep_inner import cc as dscc
from gwlfe.Input.WaterBudget.InitSnowYesterday_inner import cc as isycc
from gwlfe.Input.WaterBudget.InitSnow_inner import cc as iscc
from gwlfe.Input.WaterBudget.Percolation_inner import cc as pcc
from gwlfe.Input.WaterBudget.UnsatStor_inner import cc as usscc
from gwlfe.BMPs.Stream.UrbLoadRed_inner import cc as ulrcc
from gwlfe.MultiUse_Fxns.Runoff.WashImperv_inner import cc as wipcc
from gwlfe.MultiUse_Fxns.Runoff.WashPerv_inner import cc as wpcc

# Get the long description from README.md
with open(path.join(path.abspath(path.dirname(__file__)),
                    'README.md'), encoding='utf-8') as f:
    long_description = f.read()

tests_require = [
    'pynose == 1.5.*',
    'coverage == 4.0.3'
]

setup(
    name='gwlf-e',
    version='3.2.0',
    description='A Python port of Generalized Watersheds Loading Functions - Enhanced (MapShed)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/WikiWatershed/gwlf-e',
    author='Azavea Inc.',
    author_email='systems@azavea.com',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    keywords='gwlf-e watershed hydrology',
    packages=find_packages(exclude=['test']),
    python_requires=">=3.7",
    install_requires=[
        'certifi>=2021',
        'funcsigs==1.0.2',
        'llvmlite==0.38.*',
        'pynose==1.5.*',
        'numpy==1.21.*',
        'numba==0.55.*',
    ],
    extras_require={
        'dev': [],
        'test': tests_require,
    },
    test_suite='nose.collector',
    tests_require=tests_require,
    ext_modules=[adjcc.distutils_extension(), amc5ycc.distutils_extension(), cncc.distutils_extension(),
                 cnicc.distutils_extension(), cnpcc.distutils_extension(), dscc.distutils_extension(),
                 iscc.distutils_extension(), isycc.distutils_extension(), pcc.distutils_extension(),
                 usscc.distutils_extension(), ulrcc.distutils_extension(), wpcc.distutils_extension(),
                 wipcc.distutils_extension()]
)
