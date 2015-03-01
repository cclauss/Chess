# -*- coding: utf-8 -*-

#########################################################################
# This file is part of PhantomChess.                                    #
#                                                                       #
# PhantomChess is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  # 
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# PhantomChess is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        # 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with PhantomChess.  If not, see <http://www.gnu.org/licenses/>. #
#########################################################################

"""Some useful decorators used in Phantom."""

class named (object):
    
    def __init__(self, name):
        self.fname = name
    
    def __call__(self, f):
        
        def wrapped(*args, **kwargs):
            return f(*args, **kwargs)
        
        wrapped.__name__ = self.fname
        return wrapped

class exc_catch (object):
    """Catch exceptions.  Basically, if something goes wrong in a function and it's not one of the
    specified `passes` list, return the specified value.  If it is in the `passes` list, return
    the function (which will reraise the exception)"""
    def __init__(self, *passes, **kwargs):
        self.passes = [c.__class__ for c in passes]
        self.name = kwargs.get('name', None)
        self.ret = kwargs.get('ret', None)
        self.log = kwargs.get('log', 0)
    
    def __call__(self, f):
        retval = self.ret
        from Phantom.utils.debug import log_msg
        name = self.name if self.name is not None else f.__name__
        
        @named(name)
        def wrapped(*args, **kwargs):
            e = None
            try:
                f(*args, **kwargs)
            except Exception as e:
                if e.__class__ in self.passes:
                    return f(*args, **kwargs)
            finally:
                if (e.__class__ not in self.passes) and (e is not None):
                    if self.log:
                        log_msg('exc_catch: caught unpassed exception of type {}: {}'.format(
                                 e.__class__, e.message), self.log)
                    return retval
                elif e is not None:
                    raise e
        
        return wrapped

class default_args (object):
    
    def __init__(self, *args, **kwargs):
        self.d_args = args
        self.d_kwargs = kwargs
    
    def __call__(self, f):
        
        @named(f.__name__)
        def wrapped(*args, **kwargs):
            if args == ():
                fargs = self.d_args
            else:
                fargs = args
            if kwargs == {}:
                fkwargs = self.d_kwargs
            else:
                fkwargs = kwargs
            return f(*fargs, **fkwargs)
        
        return wrapped

