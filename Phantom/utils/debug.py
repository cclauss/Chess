# -*- coding: utf-8 -*-

"""Debug functions & decorators that provide call tracing etc
This is a base file and therefore needs to be import-clean, or at least 1-level import clean
"""

def clear_log():
    from Phantom.constants import dbgname
    import inspect, os
    orig_dir = os.getcwd()
    util_dir = os.path.split(inspect.getfile(clear_log))[0]
    
    try:
        os.chdir(util_dir)
        
        with open(dbgname, 'w') as f:
            f.write('')
        
        os.chdir(orig_dir)
    except Exception as e:
        from Chess.utils.debug import log_msg
        log_msg('Excepion {} in clear_log, unable to clear'.format(e), 1)
    finally:
        os.chdir(orig_dir)

def log_msg(msg, level):
    from Phantom.constants import dbgname, debug
    import inspect, os, sys
    
    if level > debug:
        return False
    ret = True
    
    orig_dir = os.getcwd()
    util_dir = inspect.getfile(log_msg)
    util_dir = util_dir[:util_dir.rindex('/')]
    
    try:
        os.chdir(util_dir)
        
        with open(dbgname, 'a') as f:
            f.write(msg + '\n')
        
        os.chdir(orig_dir)
    except Exception as e:
        log_msg("Exception {} in log_msg, couldn't write to file", level)
        ret = False
    finally:
        os.chdir(orig_dir)
    
    sys.stdout.write("### {}\n".format(msg))
    
    return ret


class call_trace (object):
    
    def __init__(self, level):
        self.level = level
    
    def __call__(self, f, *args, **kwargs):
        from Phantom.utils.debug import log_msg
        def wrapped(*args, **kwargs):
            log_msg('{} called with args ({}, {})'.format(f.__name__, args, kwargs), self.level)
            returned = f(*args, **kwargs)
            log_msg('{} returned {}'.format(f.__name__, returned), self.level)
            return returned
        wrapped.__name__ = f.__name__
        return wrapped

