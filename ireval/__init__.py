# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from collections import namedtuple
import ireval.io
import ireval.metrics

Weight = namedtuple('Weight', ['query', 'item', 'weight'])

def _check_duplicate(weights):
    used = set()
    for w in weights:
        if (w.query, w.item) in used:
            return False
        used.add((w.query, w.item))
    return True


def _check_missing(a, b):
    used = set()
    for x in a:
        used.add((x.query, x.item))

    for x in b:
        if (x.query, x.item) not in used:
            return False

    return True

def validate(gs, rs):
    if not _check_duplicate(gs):
        return False

    if not _check_duplicate(rs):
        return False

    if not _check_missing(gs, rs):
        return False

    if not _check_missing(rs, gs):
        return False

    return True
