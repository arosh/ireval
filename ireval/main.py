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

    if args.verbose:
        pass
    else:
        _print_mean('nDCG@3', ireval.metrics.ndcg(gs, rs, 3).values())
        _print_mean('nDCG@5', ireval.metrics.ndcg(gs, rs, 5).values())
        _print_mean('nDCG@10', ireval.metrics.ndcg(gs, rs, 10).values())
        _print_mean('nDCG@20', ireval.metrics.ndcg(gs, rs, 20).values())
        _print_mean('Q-measure', ireval.metrics.q_measure(gs, rs).values())


def main():
    _run(sys.argv)

if __name__ == '__main__':
    main()
