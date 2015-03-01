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

"""Helpers for working with directions."""

from Phantom.core.coord.vectored_lists import *

__all__ = []

def dirfinder(piece, target):
    """Locate the direction in which the target lies and return a 2-tuple of:
        (the string of the direction,
         the function that gives it)"""
    ret = ('unknown', lambda p: [0])
    if target in north(piece):
        ret = ('north', north)
    elif target in south(piece):
        ret = ('south', south)
    elif target in east(piece):
        ret = ('east', east)
    elif target in west(piece):
        ret = ('west', west)
    elif target in ne(piece):
        ret = ('ne', ne)
    elif target in nw(piece):
        ret = ('nw', nw)
    elif target in se(piece):
        ret = ('se', se)
    elif target in sw(piece):
        ret = ('sw', sw)
    return ret
__all__.append('dirfinder')

