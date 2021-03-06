# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

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
