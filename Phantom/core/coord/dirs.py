# -*- coding: utf-8 -*-

"""Helpers for working with directions."""

from Phantom.core.coord.vectored_lists import *

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

