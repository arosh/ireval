# coding: UTF-8
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os

from nose.tools import eq_, ok_

import ireval.io


def test_read_weights():
    fname = os.path.join('tests', 'weights.tsv')
    ws = ireval.io.read_weights(fname)
    eq_(5, len(ws))
    items = ['i1', 'i2', 'i3', 'i4', 'i5']
    weights = [3, 1, 0, 3, 1]
    for i, w in enumerate(ws):
        eq_('q1', w.query)
        eq_(items[i], w.item)
        eq_(weights[i], w.weight)
