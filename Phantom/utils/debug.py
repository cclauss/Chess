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

"""Debug functions & decorators that provide call tracing etc
This is a base file and therefore needs to be import-clean, or at least 1-level import clean
"""

from Phantom.constants import dbgname, phantom_dir, debug
import os
import sys

def clear_log():
    try:
        writeto = os.path.join(phantom_dir, 'utils', dbgname)
        with open(writeto, 'w') as f:
            f.write('')
    except Exception as e:
        log_msg('Excepion {} in clear_log, unable to clear'.format(e), 1, err=True)
    finally:
        os.chdir(orig_dir)

def log_msg(msg, level, **kwargs):
    err = kwargs.get('err', False)
    write = kwargs.get('write', True)
    mark = kwargs.get('mark', False)
    p = kwargs.get('p', '')
    if err and mark:
        mark = False
    
    if (level > debug) and (not err):
        return False
    ret = True
    
    if err:
         pm = '!'
    elif mark:
        pm = 'x'
    elif p:
        pm = p[0]
    else:
        pm = ' '
    msg = pm + msg
    
    if len(msg) >= 88:
        msg = msg[:88] + '\n -' + msg[88:]
    
    writeto = os.path.join(phantom_dir, 'utils', dbgname)
    
    try:
        if write:
            with open(writeto, 'a') as f:
                f.write(msg + '\n')
    except Exception as e:
        log_msg("Exception {} in log_msg, couldn't write to file", level, write=False)
        ret = False
    
    sys.stdout.write("### {}\n".format(msg))
    
    return ret


class call_trace (object):
    
    def __init__(self, level, name=None):
        self.level = level
        self.name = name
    
    def __call__(self, f, *args, **kwargs):
        from Phantom.utils.debug import log_msg
        
        def wrapped(*args, **kwargs):
            log_msg('{} called with args ({}, {})'.format(f.__name__, args, kwargs), self.level, p='{')
            returned = f(*args, **kwargs)
            log_msg('{} returned {}'.format(f.__name__, returned), self.level, p='}')
            return returned
        
        # keep the same function name to make life easier
        # *Should* use the Phantom.utils.decorators.named() decorator - but this file
        # has to be import clean, so we can't import it
        if self.name:
            wrapped.__name__ = self.name
        else:
            wrapped.__name__ = f.__name__
        
        return wrapped

