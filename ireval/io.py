# coding: UTF-8
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import codecs

import ireval


def read_tsv(fname, encoding='UTF-8', delimiter='\t', skip=0):
    ws = []
    with codecs.open(fname, encoding=encoding) as f:
        i = 0
        for line in f:
            i += 1
            if i <= skip:
                continue
            line = line.rstrip()  # remove line break characters
            if len(line) > 0:
                sp = line.split(delimiter)
                assert len(sp) == 3
                query = sp[0]
                item = sp[1]
                weight = float(sp[2])
                ws.append(ireval.Weight(query, item, weight))
    return ws

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
