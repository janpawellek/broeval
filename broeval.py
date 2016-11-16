#!/usr/bin/env python

import sys
import imp
import os
import subprocess
from datetime import datetime
import csv
import tempfile

def main():
    if len(sys.argv) != 2:
        print 'Usage: ./broeval.py <configfile>'
        return
    (cfgpath, cfgname) = os.path.split(sys.argv[1])
    (cfgname, cfgext) = os.path.splitext(cfgname)
    (cfgfile, cfgfilename, cfgdata) = imp.find_module(cfgname, [cfgpath])
    config = imp.load_module(cfgname, cfgfile, cfgfilename, cfgdata)

    sources = map(lambda (i, s): (s, config.SOURCE_BRO[i]), enumerate(config.SOURCE))
    targets = map(lambda (i, s): (s, config.TARGET_BRO[i]), enumerate(config.TARGET))

    print 'Welcome to broeval.py'
    print ''
    print 'Config: %s' % sys.argv[1]
    for src, srcb in sources:
        print 'Source: %s (with Bro %s)' % (src, 'ENABLED' if srcb else 'DISABLED')
    for tgt, tgtb in targets:
        print 'Target: %s (with Bro %s)' % (tgt, 'ENABLED' if tgtb else 'DISABLED')
    print "C'Mode: %s" % config.MODE
    print 'Epochs: %i' % config.EPOCHS
    print "Iter's: %i" % config.ITER
    print 'Size  : 10^%i bytes' % config.SIZE
    print 'Result: %s' % config.OUTFILE
    print ''

    # 1. Reset the environment (terminate Bro if still running)
    for src, srcb in sources:
        print 'Terminating Bro on source machine %s' % src
        print os.popen('./helpers/brokill.sh %s' % src).read()
    for tgt, tgtb in targets:
        print 'Terminating Bro on target machine %s' % tgt
        print os.popen('./helpers/brokill.sh %s' % tgt).read()
    csvfile = open(config.OUTFILE, 'wb')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['SOURCE', 'SOURCE_BRO', 'TARGET', 'TARGET_BRO', 'MODE', 'EPOCHS', 'ITER', 'SIZE', 'seconds', 'sourcecpu', 'sourcemem', 'targetcpu', 'targetmem'])

    # 2. Start Bro (if requested)
    for src, srcb in sources:
        if srcb:
            print 'Starting Bro on source machine %s' % src
            print os.popen('./helpers/brostart.sh %s' % src).read()
    for tgt, tgtb in targets:
        if tgtb:
            print 'Starting Bro on target machine %s' % tgt
            print os.popen('./helpers/brostart.sh %s' % tgt).read()

    for epoch in range(config.EPOCHS):
        print '---- %s - EPOCH %i - %s ----' % (sys.argv[1], epoch, datetime.now().time())
        sourcestat = [None] * len(sources)
        targetstat = [None] * len(targets)

        # If Bro is enabled, start collecting CPU / mem statistics
        for i, (src, srcb) in enumerate(sources):
            if srcb:
                sourcestat[i] = subprocess.Popen(['./helpers/brostat.sh', src], stdout=subprocess.PIPE)
        for i, (tgt, tgtb) in enumerate(targets):
            if tgtb:
                targetstat[i] = subprocess.Popen(['./helpers/brostat.sh', tgt], stdout=subprocess.PIPE)

        # Run the data transfer
        processes = []
        tempfiles = []
        seconds = []
        for i, (src, srcb) in enumerate(sources):
            processes.append([])
            tempfiles.append([])
            seconds.append([])
            for j, (tgt, tgtb) in enumerate(targets):
                processes[i].append(None)
                tempfiles[i].append(None)
                seconds[i].append(.0)
                filed, filename = tempfile.mkstemp()
                tempfiles[i][j] = [os.fdopen(filed), filename]
                processes[i][j] = subprocess.Popen(['./helpers/%s.sh' % config.MODE, src, tgt, str(config.ITER), str(config.SIZE)], stdout=subprocess.PIPE, stderr=tempfiles[i][j][0])

        for i, (src, srcb) in enumerate(sources):
            for j, (tgt, tgtb) in enumerate(targets):
                processes[i][j].wait()
                tempfiles[i][j][0].close()
                tempfiles[i][j][0] = open(tempfiles[i][j][1], 'r')
                seconds[i][j] = float(tempfiles[i][j][0].readlines()[-1].strip())
                tempfiles[i][j][0].close()
                os.remove(tempfiles[i][j][1])
                print 'source %s, target %s: %.2f seconds.' % (src, tgt, seconds[i][j])

        # If Bro is enabled, stop collecting CPU / mem statistics
        sourcecpu = [.0] * len(sources)
        sourcemem = [.0] * len(sources)
        targetcpu = [.0] * len(targets)
        targetmem = [.0] * len(targets)
        for i, (src, srcb) in enumerate(sources):
            if srcb:
                sourcestat[i].kill()
                outs, errs = sourcestat[i].communicate()
                lines = outs.split('\n')
                linecount = 0
                for line in lines:
                    if line and line.split()[0] != '%CPU':
                        linecount += 1
                        sourcecpu[i] += float(line.split()[0].replace(',', '.'))
                        sourcemem[i] += float(line.split()[1])
                sourcecpu[i] /= linecount
                sourcemem[i] /= linecount
                print 'Bro @ source %s took on average %.2f%% CPU and %.0f KB of physical memory.' % (src, sourcecpu[i], sourcemem[i])
        for i, (tgt, tgtb) in enumerate(targets):
            if tgtb:
                targetstat[i].kill()
                outs, errs = targetstat[i].communicate()
                lines = outs.split('\n')
                linecount = 0
                for line in lines:
                    if line and line.split()[0] != '%CPU':
                        linecount += 1
                        targetcpu[i] += float(line.split()[0].replace(',', '.'))
                        targetmem[i] += float(line.split()[1])
                targetcpu[i] /= linecount
                targetmem[i] /= linecount
                print 'Bro @ target %s took on average %.2f%% CPU and %.0f KB of physical memory.' % (tgt, targetcpu[i], targetmem[i])

        for i, (src, srcb) in enumerate(sources):
            for j, (tgt, tgtb) in enumerate(targets):
                csvwriter.writerow([src, srcb, tgt, tgtb, config.MODE, config.EPOCHS, config.ITER, config.SIZE, seconds[i][j], sourcecpu[i], sourcemem[i], targetcpu[j], targetmem[j]])
        print '\n'

    # Terminate Bro
    csvfile.close()
    for src, srcb in sources:
        if srcb:
            print 'Terminating Bro on source machine %s' % src
            print os.popen('./helpers/brokill.sh %s' % src).read()
    for tgt, tgtb in targets:
        if tgtb:
            print 'Terminating Bro on target machine %s' % tgt
            print os.popen('./helpers/brokill.sh %s' % tgt).read()

if __name__ == '__main__':
    main()

