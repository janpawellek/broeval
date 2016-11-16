#!/usr/bin/env python

LATEX = True

import sys
import os
import csv
import re
from scipy import stats

def main():
    if len(sys.argv) < 3 or not len(sys.argv) % 2:
        print 'Usage: ./results_aggregate.py <resultfile_nobro_1, resultfile_nobro_2, ..., resultfile_bro_1, resultfile_bro_2, ...>'
        print 'e.g. ./results_aggregate.py runs/seq-nobro-iter*.result.csv runs/seq-bro-iter*.result.csv'
        return
    firstlen = len(sys.argv[1:]) / 2
    resultfns = [(sys.argv[1:][i], sys.argv[1:][firstlen+i]) for i in range(firstlen)]

    if LATEX:
        print "LaTeX output is enabled. To generate a CSV instead, set 'LATEX = False' at the beginning of this script file."
    else:
        print "file_bro, total_nobro, total_bro, avgsec_nobro, avgsec_bro, avgsec_diff, statistic, pvalue, avgsrccpu, avgsrcmem, avgtgtcpu, avgtgtmem"
    for resultfn in resultfns:
        resultf_nobro = open(resultfn[0])
        resultf_bro = open(resultfn[1])
        reader_nobro = csv.DictReader(resultf_nobro)
        reader_bro = csv.DictReader(resultf_bro)
        total_bro = 0
        total_nobro = 0
        avgsec_nobro = .0
        avgsec_bro = .0
        avgsrccpu = .0
        avgsrcmem = .0
        avgtgtcpu = .0
        avgtgtmem = .0
        a = []
        b = []
        for row in reader_nobro:
            total_nobro += 1
            avgsec_nobro += float(row['seconds'])
            a.append(float(row['seconds']))
        for row in reader_bro:
            total_bro += 1
            avgsec_bro += float(row['seconds'])
            b.append(float(row['seconds']))
            avgsrccpu += float(row['sourcecpu'])
            avgsrcmem += float(row['sourcemem'])
            avgtgtcpu += float(row['targetcpu'])
            avgtgtmem += float(row['targetmem'])
        avgsec_nobro /= total_nobro
        avgsec_bro /= total_bro
        avgsrccpu /= total_bro
        avgsrcmem /= total_bro
        avgtgtcpu /= total_bro
        avgtgtmem /= total_bro
        statistic, pvalue = stats.ttest_ind(a, b, equal_var=False)
        if LATEX:
            niter = int(re.sub(r'\D', '', os.path.basename(resultfn[1])))
            print "%i & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\" % (niter, avgsec_nobro, avgsec_bro, (avgsec_bro-avgsec_nobro), pvalue, avgsrccpu, avgsrcmem, avgtgtcpu, avgtgtmem)
        else:
            print "%s, %i, %i, %.2f, %.2f, %.2f, %.2f, %.5f, %.2f, %.2f, %.2f, %.2f" % (resultfn[1], total_nobro, total_bro, avgsec_nobro, avgsec_bro, (avgsec_bro-avgsec_nobro), statistic, pvalue, avgsrccpu, avgsrcmem, avgtgtcpu, avgtgtmem)

        resultf_nobro.close()
        resultf_bro.close()

if __name__ == '__main__':
    main()

