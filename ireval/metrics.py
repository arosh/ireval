# coding: UTF-8
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import math

import ireval


def _group_by_query(ws):
    by_query = {}
    for w in ws:
        by_query.setdefault(w.query, [])
        by_query[w.query].append(w)
    return by_query


def _ndcg_one_query(gs, rs, k):
    gs_sorted = sorted([w.weight for w in gs], reverse=True)
    denom = sum(x / math.log(r + 1)
                for x, r in zip(gs_sorted, range(1, k + 1)))

    weight_dict = {}
    for w in gs:
        weight_dict[w.item] = w.weight

    rs_sorted = [weight_dict[w.item]
                 for w in sorted(rs, key=lambda w: w.weight, reverse=True)]
    numer = sum(x / math.log(r + 1)
                for x, r in zip(rs_sorted, range(1, k + 1)))

    return numer / denom


def ndcg(gs, rs, k):
    assert ireval.validate(gs, rs)
    # {query -> Weight}
    gs_query = _group_by_query(gs)
    rs_query = _group_by_query(rs)

    assert gs_query.keys() == rs_query.keys()
    queries = gs_query.keys()

    # {query -> nDCG}
    scores = {}
    for query in queries:
        scores[query] = _ndcg_one_query(gs_query[query], rs_query[query], k)

    return scores
