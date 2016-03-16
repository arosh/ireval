# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from nose.tools import eq_, ok_

import ireval
import tests


def test_validate_missing():
    queries = ['q1', 'q1', 'q1']
    items = ['i1', 'i2', 'i3']
    weights = [3, 2, 1]
    gs = []
    for q, i, w in zip(queries, items, weights):
        gs.append(ireval.Weight(q, i, w))

    queries = ['q1', 'q1']
    items = ['i1', 'i2']
    weights = [3, 2]
    rs = []
    for q, i, w in zip(queries, items, weights):
        rs.append(ireval.Weight(q, i, w))

    ok_(not ireval.validate(gs, rs))


def test_validate_duplicate():
    queries = ['q1', 'q1', 'q1']
    items = ['i1', 'i2', 'i3']
    weights = [3, 2, 1]
    gs = []
    for q, i, w in zip(queries, items, weights):
        gs.append(ireval.Weight(q, i, w))

    queries = ['q1', 'q1', 'q1', 'q1']
    items = ['i1', 'i2', 'i3', 'i3']
    weights = [3, 2, 1, 0]
    rs = []
    for q, i, w in zip(queries, items, weights):
        rs.append(ireval.Weight(q, i, w))

    ok_(not ireval.validate(gs, rs))


def test_validate_ok():
    gs = tests.test_io.test_read_weights()
    rs = tests.test_io.test_read_runs()
    ok_(ireval.validate(gs, rs))


def test_queries():
    gs = tests.test_io.test_read_weights()
    ok_(set(['q1', 'q2']), ireval.queries(gs))
