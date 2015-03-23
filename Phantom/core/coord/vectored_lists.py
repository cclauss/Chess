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
    
@call_trace(9)
@integer_args
def ne(piece):
    iterto = min(grid_width-piece.coord.x, grid_height-piece.coord.y)
    return [Coord(piece.coord.x+i, piece.coord.y+i) for i in xrange(1, iterto)]

@call_trace(9)
@integer_args
def se(piece):
    iterto = min(grid_width-piece.coord.x, piece.coord.y)
    return [Coord(piece.coord.x+i, piece.coord.y-i) for i in xrange(1, iterto+1)]

@call_trace(9)
@integer_args
def nw(piece):
    iterto = min(piece.coord.x, grid_height-piece.coord.y)
    return [Coord(piece.coord.x-i, piece.coord.y+i) for i in xrange(1, iterto+1)]

@call_trace(9)
@integer_args
def sw(piece):
    iterto = min(piece.coord.x, piece.coord.y)
    return [Coord(piece.coord.x-i, piece.coord.y-i) for i in xrange(1, iterto+1)]

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
    return [c for c in all if not c in known]

__all__ = [func.__name__ for func in (north, south, east, west, ne, se, nw, sw, unknown)]
    
