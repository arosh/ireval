# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import os

from nose.tools import eq_, ok_

import ireval


def test_read_weights():
    fname = os.path.join('tests', 'weights.tsv')
    gs = ireval.io.read_tsv(fname)
    eq_(10, len(gs))
    queries = ['q1', 'q1', 'q1', 'q1', 'q1', 'q2', 'q2', 'q2', 'q2', 'q2']
    items = ['i1', 'i2', 'i3', 'i4', 'i5', 'i1', 'i2', 'i3', 'i4', 'i5']
    weights = [3, 1, 0, 3, 1, 2, 1, 3, 0, 1]
    for i, w in enumerate(gs):
        eq_(queries[i], w.query)
        eq_(items[i], w.item)
        eq_(weights[i], w.weight)
    return gs


def test_read_runs():
    fname = os.path.join('tests', 'run.tsv')
    rs = ireval.io.read_tsv(fname, skip=1)
    eq_(10, len(rs))
    queries = ['q1', 'q1', 'q1', 'q1', 'q1', 'q2', 'q2', 'q2', 'q2', 'q2']
    items = ['i1', 'i2', 'i3', 'i4', 'i5', 'i1', 'i2', 'i3', 'i4', 'i5']
    weights = [0.8, 0.4, 1.0, 0.6, 0.2, 1.0, 0.8, 0.6, 0.4, 0.2]
    for i, r in enumerate(rs):
        eq_(queries[i], r.query)
        eq_(items[i], r.item)
        eq_(weights[i], r.weight)
    return rs
