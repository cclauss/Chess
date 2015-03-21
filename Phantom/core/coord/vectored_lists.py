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

"""Squares in a given direction."""

from Phantom.core.coord.point import Coord, Grid
from Phantom.constants import grid_height, grid_width
from Phantom.utils.decorators import integer_args
from Phantom.utils.debug import call_trace

__all__ = []

# implementation detail 2, 3

@call_trace(9)
@integer_args
def north(piece):
    return [Coord(piece.coord.x, i) for i in xrange(piece.coord.y+1, grid_height)]

@call_trace(9)
@integer_args
def south(piece):
    return [Coord(piece.coord.x, i) for i in xrange(piece.coord.y-1, -1, -1)]

@call_trace(9)
@integer_args
def east(piece):
    return [Coord(i, piece.coord.y) for i in xrange(piece.coord.x+1, grid_width)]

@call_trace(9)
@integer_args
def west(piece):
    return [Coord(i, piece.coord.y) for i in xrange(piece.coord.x-1, -1, -1)]

for func in (north, south, east, west):
    __all__.append(func.__name__)
    
@call_trace(9)
@integer_args
def ne(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    iterto = min(grid_width-x, grid_height-y)
    for i in range(1, iterto):
        ret.append(Coord(x+i, y+i))
    return ret
__all__.append('ne')

@call_trace(9)
@integer_args
def se(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    iterto = min(grid_width-x, y)
    for i in range(1, iterto+1):
        ret.append(Coord(x+i, y-i))
    return ret
__all__.append('se')

@call_trace(9)
@integer_args
def nw(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    iterto = min(x, grid_height-y)
    for i in range(1, iterto+1):
        ret.append(Coord(x-i, y+i))
    return ret
__all__.append('nw')

@call_trace(9)
@integer_args
def sw(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    iterto = min(x, y)
    for i in range(1, iterto+1):
        ret.append(Coord(x-i, y-i))
    return ret
__all__.append('sw')

@call_trace(9)
@integer_args
def unknown(piece):
    def join(*args):
        ret = []
        for arg in args:
            ret.extend(arg(piece))
    known = join(north, south, east, west, ne, se, nw, sw)
    alltiles = piece.owner.board.tiles
    all = [tile.coord for tile in alltiles]
    ret = [c for c in all if not c in known]
    return ret
__all__.append('unknown')
    
