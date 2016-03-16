# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import sys
import numpy

import ireval


def _parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--goldstandard', dest='gsfile', required=True)
    parser.add_argument('-r', '--rankedlist', dest='rsfile', required=True)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--skip', default=1, metavar='N',
                        type=int, help='Skip first N lines in ranked list (-r/--rankedlist) (default=1)')
    return parser.parse_args(argv)


def _print_mean(name, values):
    mean = numpy.mean(values)
    print('{}={:.4f}'.format(name, mean))


def _run(argv):
    args = _parse_args(argv[1:])
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
            print('{}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}'.format(q, ndcg_at3[q], ndcg_at5[q], ndcg_at10[q], ndcg_at20[q], q_measure[q]))
    else:
        _print_mean('nDCG@3', ndcg_at3.values())
        _print_mean('nDCG@5', ndcg_at5.values())
        _print_mean('nDCG@10', ndcg_at10.values())
        _print_mean('nDCG@20', ndcg_at20.values())
        _print_mean('Q-measure', q_measure.values())


def main():
    _run(sys.argv)

if __name__ == '__main__':
    main()
