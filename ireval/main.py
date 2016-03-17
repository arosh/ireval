# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import sys
import numpy

import ireval


def _parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--goldstandard',
                        metavar='GOLD_STANDARD', dest='gsfile', required=True)
    parser.add_argument('-r', '--rankedlist',
                        metavar='RANKED_LIST', dest='rsfile', required=True)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--skip', default=1, metavar='N',
                        type=int, help='Skip first N lines in ranked list RANKED_LIST (default=1)')
    return parser.parse_args(argv)


def _run(argv):
    args = _parse_args(argv)
    gs = ireval.io.read_tsv(args.gsfile, skip=0)
    rs = ireval.io.read_tsv(args.rsfile, skip=args.skip)

    ndcg_at3 = ireval.metrics.ndcg(gs, rs, 3)
    ndcg_at5 = ireval.metrics.ndcg(gs, rs, 5)
    ndcg_at10 = ireval.metrics.ndcg(gs, rs, 10)
    ndcg_at20 = ireval.metrics.ndcg(gs, rs, 20)
    q_measure = ireval.metrics.q_measure(gs, rs)

    if args.verbose:
        queries = sorted(ireval.queries(gs))
        print('query\tnDCG@3\tnDCG@5\tnDCG@10\tnDCG@20\tQ-measure')
        for q in queries:
            ts = []
            ts.append(q)

            _format = lambda values: '{:.4f}'.format(values)
            ts.append(_format(ndcg_at3[q]))
            ts.append(_format(ndcg_at5[q]))
            ts.append(_format(ndcg_at10[q]))
            ts.append(_format(ndcg_at20[q]))
            ts.append(_format(q_measure[q]))

            print('\t'.join(ts))
    else:
        def _format(name, query2metrics):
            mean = numpy.mean(query2metrics.values())
            return '{}={:.4f}'.format(name, mean)

        print(_format('nDCG@3', ndcg_at3))
        print(_format('nDCG@5', ndcg_at5))
        print(_format('nDCG@10', ndcg_at10))
        print(_format('nDCG@20', ndcg_at20))
        print(_format('Q-measure', q_measure))


def main():
    _run(sys.argv[1:])

if __name__ == '__main__':
    main()
