# -*- coding: utf-8 -*-

"""Run all the tests in the Phantom.tests"""

from Phantom.utils.debug import log_msg, clear_log
import os
import inspect

def main(*args):
    clear_log()
    testdir = inspect.getfile(main)
    testdir, dirname = os.path.split(testdir)
    
    for f in os.listdir(testdir):
        if (f == dirname) or (f == '__init__.py'):
            continue
        else:
            mn = f[:f.index('.')]
            m = __import__(mn)
            m.main(False)

if __name__ == '__main__':
    main()

