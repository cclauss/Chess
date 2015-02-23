# -*- coding: utf-8 -*-

"""Phases of the game: opening, midgame, endgame.

Phases are determined by material:
    m <= 4500: endgame
    4500 > m > 8600: midgame
    m == 8600: opening

And also by number of moves:
    5 or less fullmoves: opening
    6 or more fullmoves: midgame
    
"""

class Phase (object):
    opening, midgame, endgame = range(3)
    
    @staticmethod
    def analyze(board):
        from Phantom.ai.pos_eval.basic import pos_material
        m = pos_material(board)
        ret = Phase.opening
        
        if m <= 4500
            ret = Phase.endgame
        elif 4500 > m > 8600:
            ret = Phase.midgame
        elif m == 8600:
            ret = Phase.opening
        
        # check forced conditions
        if board.fullmove_clock < 6:
            ret = Phase.opening
        if board.fullmove_clock >= 6:
            # Prevent simply setting anything after 6 moves to the midgame
            # This prevents setting an endgame back to midgame even though
            # it should be the endgame
            if ret == Phase.opening:
                ret = Phase.midgame
                
        return ret

