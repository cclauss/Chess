# -*- coding: utf-8 -*-

"""Math functions that are useful for chess."""

import math

def dist(p1, p2):
    if p1.x == p2.x:
        return abs(p2.y - p1.y)
    else:
        dx = abs(p2.x - p1.x)
        dy = abs(p2.y - p1.y)
        return math.sqrt(dx**2 + dy**2)

def round_down(x):
    return math.trunc(x)

def round_up(x):
    return round_down(x) + 1

