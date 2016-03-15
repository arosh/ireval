# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals
from setuptools import setup, find_packages

setup(
    name='ireval',
    version='0.0.0',
    description='Collection of Evaluation Metrics for Information Retrieval',
    url='https://github.com/arosh/ireval',
    license='BSD 3-Clause',
    packages=find_packages(exclude=['tests']),
    tests_require=['nose'],
    test_suite = 'nose.collector'
)
