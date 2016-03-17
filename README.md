# IREval

Collection of Evaluation Metrics for Information Retrieval

## List of Metrics

* nDCG [Järvelin, 2002]
* Q-measure [Sakai, 2007]

## How to Install

```
$ pip install (--user) git+https://github.com/arosh/ireval.git
```

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
$ git clone https://github.com/arosh/ireval.git
$ cd path/to/ireval
$ python setup.py test
```

## ToDo

* confidence interval
* p-value
* effect size

## License

This software is released under the BSD 3-Clause License.

## References

* [Järvelin, K. and Kekäläinen, J.: Cumulated gain-based evaluation of IR techniques, ACM Transactions on Information Systems, Vol.20, pp.422-446 (2002).](http://dx.doi.org/10.1145/582415.582418)
* [Sakai, T.: On the reliability of information retrieval metrics based on graded relevance, Information Processing & Management, Vol.43, pp.531-548 (2007).](http://dx.doi.org/10.1016/j.ipm.2006.07.020)
* [Evaluation Measures - NTCIR-12 MobileClick-2](http://www.mobileclick.org/home/task)
* [NTCIREVAL: NTCIR Project Tools](http://research.nii.ac.jp/ntcir/tools/ntcireval-en.html)
* [Sakai, T.: Information Retrieval Test Collections and Evaluation Metrics: A Tutorial, IPSJ SIG Technical Reports, pp.1-8 (2008).](http://id.nii.ac.jp/1001/00040050/)
* [Sakai, T.: Statistical reform in information retrieval?, ACM SIGIR Forum Vol.48, pp.3-12 (2014).](http://dx.doi.org/10.1145/2641383.2641385)
