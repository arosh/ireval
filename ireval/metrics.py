# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy
import ireval


def _group_by_query(ws):
    by_query = {}
    for w in ws:
        by_query.setdefault(w.query, [])
        by_query[w.query].append(w)
    return by_query


def _ndcg_one_query(gs, rs, k):
    assert len(gs) == len(rs)

    weight_dict = {}
    for w in gs:
        weight_dict[w.item] = w.weight
    rs = [weight_dict[w.item]
          for w in sorted(rs, key=lambda w: w.weight, reverse=True)]
    gs = [weight_dict[w.item]
          for w in sorted(gs, key=lambda w: w.weight, reverse=True)]

    numer = sum(x / numpy.log(r + 1)
                for x, r in zip(rs, range(1, k + 1)))
    denom = sum(x / numpy.log(r + 1)
                for x, r in zip(gs, range(1, k + 1)))

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


def _q_measure_one_query(gs, rs, beta):
    assert len(gs) == len(rs)

    weight_dict = {}
    for w in gs:
        weight_dict[w.item] = w.weight
    rs = [weight_dict[w.item]
          for w in sorted(rs, key=lambda w: w.weight, reverse=True)]
    gs = [weight_dict[w.item]
          for w in sorted(gs, key=lambda w: w.weight, reverse=True)]

    IsRel = lambda x: 1 if x > 0 else 0
    sigma = []
    M = len(gs)
    for r in range(M):
        numer = []
        denom = []
        for r2 in range(r + 1):
            numer.append(beta * rs[r2] + IsRel(rs[r2]))
            denom.append(beta * gs[r2] + 1.0)
        sigma.append(IsRel(rs[r]) * sum(numer) / sum(denom))

    R = sum(IsRel(x) for x in rs)
    return sum(sigma) / R


def q_measure(gs, rs, beta=1.0):
    assert ireval.validate(gs, rs)
    # {query -> Weight}
    gs_query = _group_by_query(gs)
    rs_query = _group_by_query(rs)

    assert gs_query.keys() == rs_query.keys()
    queries = gs_query.keys()

    # {query -> Q-measure}
    scores = {}
    for query in queries:
        scores[query] = _q_measure_one_query(
            gs_query[query], rs_query[query], beta)

    return scores
