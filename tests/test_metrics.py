# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from nose.tools import assert_almost_equal, eq_, ok_

import ireval
import tests


def test_ndcg_at_5():
    k = 5
    # q1: [0, 3, 3, 1, 1]
    # q2: [2, 1, 3, 0, 1]
    gs = tests.test_io.test_read_weights()
    rs = tests.test_io.test_read_runs()
    ms = ireval.metrics.ndcg(gs, rs, k)
    # nDCG = nDCG/iDCG
    # DCG = 3/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) + 3/log2(4+1) + 1/log2(5+1)
    # iDCG = 3/log2(1+1) + 3/log2(2+1) + 1/log2(3+1) + 1/log2(4+1) + 0/log2(5+1)
    eq_(2, len(ms))
    assert_almost_equal(4.210318626 / 5.823465819, ms['q1'])
    assert_almost_equal(4.517782561 / 5.192536065, ms['q2'])


def test_ndcg_at_3():
    k = 3
    # q1: [0, 3, 3, 1, 1]
    # q2: [2, 1, 3, 0, 1]
    gs = tests.test_io.test_read_weights()
    rs = tests.test_io.test_read_runs()
    ms = ireval.metrics.ndcg(gs, rs, k)
    # nDCG = nDCG/iDCG
    # DCG = 3/log2(1+1) + 1/log2(2+1) + 0/log2(3+1)
    # iDCG = 3/log2(1+1) + 3/log2(2+1) + 1/log2(3+1)
    eq_(2, len(ms))
    assert_almost_equal(3.392789261 / 5.392789261, ms['q1'])
    assert_almost_equal(4.130929754 / 4.761859507, ms['q2'])


def test_q_measure():
    # q1: [0, 3, 3, 1, 1]
    # q2: [2, 1, 3, 0, 1]
    gs = tests.test_io.test_read_weights()
    rs = tests.test_io.test_read_runs()
    ms = ireval.metrics.q_measure(gs, rs)
    eq_(2, len(ms))
    assert_almost_equal((4 / 8 + 8 / 10 + 10 / 12 + 12 / 13) / 4, ms['q1'])
    assert_almost_equal((3 / 4 + 5 / 7 + 9 / 9 + 11 / 12) / 4, ms['q2'])
