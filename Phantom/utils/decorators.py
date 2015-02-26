# -*- coding: utf-8 -*-

"""Some useful decorators used in Phantom."""

class exc_catch (object):
    """Catch exceptions.  Basically, if something goes wrong in a function and it's not one of the
    specified `passes` list, return the specified value.  If it is in the `passes` list, return
    the function (which will reraise the exception)"""
    def __init__(self, *passes, **kwargs):
        self.passes = [c.__class__ for c in passes]
        self.name = kwargs.get('name', None)
        self.ret = kwargs.get('ret', None)
    
    def __call__(self, f):
        retval = self.ret
        
        def wrapped(*args, **kwargs):
            e = None
            try:
                f(*args, **kwargs)
            except Exception as e:
                if e.__class__ in self.passes:
                    return f(*args, **kwargs)
            finally:
                if e.__class__ not in self.passes:
                    return retval
                else:
                    raise e
        
        if self.name:
            wrapped.__name__ = self.name
        else:
            wrapped.__name__ = f.__name__
        
        return wrapped

