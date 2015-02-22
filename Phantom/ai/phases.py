# -*- coding: utf-8 -*-

"""Phases of the game: opening, midgame, endgame.

Phases are determined by material:
    m <= 4500: endgame
    4500 > m > 8600: midgame
    m == 8600: opening
"""

class Phase (object):
    opening, midgame, endgame = range(3)
    
    @staticmethod
    def analyze(board):
        from Phantom.ai.pos_eval.basic import pos_material
        m = pos_material(board)
        ret = Phase.opening
        if m <= 4500:
            ret = Phase.endgame
        elif 4500 > m > 8600:
            ret = Phase.midgame
        elif m == 8600:
            ret = Phase.opening
        return ret

