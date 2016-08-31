#!/usr/bin/env python

import sys
import imp
import os
from datetime import datetime

def main():
    if len(sys.argv) != 2:
        print 'Usage: ./broeval.py <configfile>'
        return
    (cfgpath, cfgname) = os.path.split(sys.argv[1])
    (cfgname, cfgext) = os.path.splitext(cfgname)
    (cfgfile, cfgfilename, cfgdata) = imp.find_module(cfgname, [cfgpath])
    config = imp.load_module(cfgname, cfgfile, cfgfilename, cfgdata)

    print 'Welcome to broeval.py'
    print ''
    print 'Config: %s' % sys.argv[1]
    print 'Source: %s (with Bro %s)' % (config.SOURCE, 'ENABLED' if config.SOURCE_BRO else 'DISABLED')
    print 'Target: %s (with Bro %s)' % (config.TARGET, 'ENABLED' if config.TARGET_BRO else 'DISABLED')
    print "C'Mode: %s" % config.MODE
    print 'Epochs: %i' % config.EPOCHS
    print "Iter's: %i" % config.ITER
    print 'Size  : 10^%i bytes' % config.SIZE
    print 'Result: %s' % config.OUTFILE
    print ''

    # 1. Reset the environment (terminate Bro if still running)
    print 'Terminating Bro on source machine %s' % config.SOURCE
    print os.popen('./helpers/brokill.sh %s' % config.SOURCE).read()
    print 'Terminating Bro on target machine %s' % config.TARGET
    print os.popen('./helpers/brokill.sh %s' % config.TARGET).read()

    # 2. Start Bro (if requested)
    if config.SOURCE_BRO:
        print 'Starting Bro on source machine %s' % config.SOURCE
        print os.popen('./helpers/brostart.sh %s' % config.SOURCE).read()
    if config.TARGET_BRO:
        print 'Starting Bro on target machine %s' % config.TARGET
        print os.popen('./helpers/brostart.sh %s' % config.TARGET).read()

    for epoch in range(config.EPOCHS):
        print '---- EPOCH %i - %s ----' % (epoch, datetime.now().time())
        output = os.popen('./helpers/%s.sh %s %s %i %i 2>&1' % (config.MODE, config.SOURCE, config.TARGET, config.ITER, config.SIZE)).read()
        print '    ' + output.replace('\n', '\n    ')
        seconds = float(output.split('\n')[-2])
        print 'Epoch %i took %.2f seconds.\n' % (epoch, seconds)

    # Terminate Bro
    print 'Terminating Bro on source machine %s' % config.SOURCE
    print os.popen('./helpers/brokill.sh %s' % config.SOURCE).read()
    print 'Terminating Bro on target machine %s' % config.TARGET
    print os.popen('./helpers/brokill.sh %s' % config.TARGET).read()

if __name__ == '__main__':
    main()

