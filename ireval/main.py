# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import sys

import ireval


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--goldstandard', dest='gsfile', required=True)
    parser.add_argument('-r', '--rankedlist', dest='rsfile', required=True)
    parser.add_argument('--skip', default=1, metavar='N',
                        type=int, help='Skip first N lines in ranked list (-r/--rankedlist) (default=1)')
    return parser.parse_args(argv)


def _run(argv):
    args = parse_args(argv)
    print(args)

def main():
    _run(sys.argv)

if __name__ == '__main__':
    main()
