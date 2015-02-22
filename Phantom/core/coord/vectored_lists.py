# -*- coding: utf-8 -*-

"""Squares in a given direction."""

from Phantom.core.coord.point import Coord, Grid
from Phantom.constants import grid_height, grid_width

# implementation detail 2, 3

def north(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    for i in range(y+1, grid_height):
        ret.append(Coord(x, i))
    return ret

def south(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    for i in range(y-1, -1, -1):
        ret.append(Coord(x, i))
    return ret

def east(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    for i in range(x+1, grid_width):
        ret.append(Coord(i, y))
    return ret

def west(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    for i in range(x-1, -1, -1):
        ret.append(Coord(i, y))
    return ret

def ne(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    iterto = min(grid_width-x, grid_height-y)
    for i in range(1, iterto):
        ret.append(Coord(x+i, y+i))
    return ret

def se(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    iterto = min(grid_width-x, y)
    for i in range(1, iterto+1):
        ret.append(Coord(x+i, y-i))
    return ret

def nw(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    iterto = min(x, grid_height-y)
    for i in range(1, iterto+1):
        ret.append(Coord(x-i, y+i))
    return ret

def sw(piece):
    x = piece.coord.x
    y = piece.coord.y
    ret = []
    iterto = min(x, y)
    for i in range(1, iterto+1):
        ret.append(Coord(x-i, y-i))
    return ret

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
    
