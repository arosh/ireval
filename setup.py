# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from setuptools import find_packages, setup

setup(
    name='ireval',
    version='0.0.1',
    description='Collection of Evaluation Metrics for Information Retrieval',
    url='https://github.com/arosh/ireval',
    license='BSD 3-Clause',
    packages=find_packages(exclude=['tests']),
    install_requires=['numpy'],
    tests_require=['nose'],
    test_suite='nose.collector',
    entry_points='''
    [console_scripts]
    ireval = ireval.main:main
    '''
)
