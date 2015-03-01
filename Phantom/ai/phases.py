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

"""Phases of the game: opening, midgame, endgame.

Phases are determined by material:
    m <= 4500: endgame
    4500 > m > 8600: midgame
    m == 8600: opening

By number of moves:
    5 or less fullmoves: opening
    6 or more fullmoves: midgame
    
or if both queens have been moved:
    neither queen has been moved, or one has been but not the other: opening
    both queens have been moved: midgame
    
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
        
        # check move clock
        if board.fullmove_clock < 6:
            ret = Phase.opening
        if board.fullmove_clock >= 6:
            # Prevent simply setting anything after 6 moves to the midgame
            # This prevents setting an endgame back to midgame even though
            # it should be the endgame
            if ret == Phase.opening:
                ret = Phase.midgame
            
        # check queen movement status
        queens = []
        for piece in board.pieces:
            if piece.ptype == 'queen':
                queens.append(piece)
        if all([not q.firstmove for q in queens]):
            if ret == Phase.opening:
                ret = Phase.midgame
                
        return ret

