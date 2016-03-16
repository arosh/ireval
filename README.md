# IREval

Collection of Evaluation Metrics for Information Retrieval

## List of Metrics

* nDCG [Järvelin, 2002]
* Q-measure [Sakai, 2007]

## Example

```
$ ireval -g examples/weights.tsv -r examples/run.tsv 
nDCG@3=0.7483
nDCG@5=0.7965
nDCG@10=0.7965
nDCG@20=0.7965
Q-measure=0.8047
```

```
$ ireval -v -g examples/weights.tsv -r examples/run.tsv 
query nDCG@3  nDCG@5  nDCG@10 nDCG@20 Q-measure
q1  0.6291  0.7230  0.7230  0.7230  0.7641
q2  0.8675  0.8701  0.8701  0.8701  0.8452
```

## Help

```
$ ireval -h
usage: ireval [-h] -g GOLD_STANDARD -r RANKED_LIST [-v] [--skip N]

optional arguments:
  -h, --help            show this help message and exit
  -g GOLD_STANDARD, --goldstandard GOLD_STANDARD
  -r RANKED_LIST, --rankedlist RANKED_LIST
  -v, --verbose         Show metrics in each queries
  --skip N              Skip first N lines in RANKED_LIST (default=1)
```

## How to Test

```
nosetest -v
```

## License

This software is released under the BSD 3-Clause License.

## References

* NTCIR-12 MobileClick-2, http://www.mobileclick.org/home/task
* Järvelin, K. and Kekäläinen, J.: Cumulated gain-based evaluation of IR techniques, ACM Transactions on Information Systems, Vol.20, pp.422-446 (2002).
* Sakai, T.: On the reliability of information retrieval metrics based on graded relevance, Information Processing & Management, Vol.43, pp.531-548 (2007).
* 酒井哲也：情報検索テストコレクションと評価指標，情報処理学会研究報告，pp.1-8 (2008).
* NTCIREVAL: NTCIR Project Tools, http://research.nii.ac.jp/ntcir/tools/ntcireval-en.html
