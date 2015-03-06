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

__all__ = []

# implementation detail 2, 3

@integer_args
def north(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    for i in range(y+1, grid_height):
        ret.append(Coord(x, i))
    return ret
__all__.append('north')

@integer_args
def south(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    for i in range(y-1, -1, -1):
        ret.append(Coord(x, i))
    return ret
__all__.append('south')

@integer_args
def east(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    for i in range(x+1, grid_width):
        ret.append(Coord(i, y))
    return ret
__all__.append('east')

@integer_args
def west(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    for i in range(x-1, -1, -1):
        ret.append(Coord(i, y))
    return ret
__all__.append('west')

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
    
