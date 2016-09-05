#!/usr/bin/env python

import sys
import os
import csv

def main():
    if len(sys.argv) != 2:
        print 'Usage: ./plotter.py <resultfile>'
        return
    resultfn = sys.argv[1]

    print 'Welcome to plotter.py'
    print ''
    print 'Data file: %s' % resultfn
    print ''

    # 1. Read CSV file
    resultf = open(resultfn)
    reader = csv.DictReader(resultf)
    total = 0
    avgsec = .0
    avgsrccpu = .0
    avgsrcmem = .0
    avgtgtcpu = .0
    avgtgtmem = .0
    for row in reader:
        total += 1
        avgsec += float(row['seconds'])
        avgsrccpu += float(row['sourcecpu'])
        avgsrcmem += float(row['sourcemem'])
        avgtgtcpu += float(row['targetcpu'])
        avgtgtmem += float(row['targetmem'])
    avgsec /= total
    avgsrccpu /= total
    avgsrcmem /= total
    avgtgtcpu /= total
    avgtgtmem /= total
    print 'Total lines: %i' % total
    print 'Avg seconds: %.2f' % avgsec
    print 'Avg src cpu: %.2f' % avgsrccpu
    print 'Avg src mem: %.2f' % avgsrcmem
    print 'Avg tgt cpu: %.2f' % avgtgtcpu
    print 'Avg tgt mem: %.2f' % avgtgtmem

    resultf.close()

if __name__ == '__main__':
    main()

