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

"""Player class."""

from Phantom.constants import *
from Phantom.core.exceptions import InvalidMove, LogicError
from Phantom.core.coord.point import Coord
from Phantom.functions import round_down, dist
from Phantom.utils.debug import call_trace, log_msg
import uuid

__all__ = []

class Side (object):
    
    def __init__(self, color):
        if isinstance(color, Side):
            self.color = color.color
            self.tilecolor = color.tilecolor
            return
        if 'w' in color.lower():
            self.color = 'white'
        elif 'b' in color.lower():
            self.color = 'black'
        else:
            raise LogicError("Couldn't identify color: {}".format(color),
                             'Phantom.core.players.Side.__init__()')
        self.tilecolor = grid_colors[self.color]
    
    def __eq__(self, other):
        if isinstance(other, Side):
            return self.color == other.color
        elif isinstance(other, str):
            return self.color == other
        else:
            raise TypeError("Side can't be compared with type {}".format(type(other)))
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __repr__(self):
        return "Side({})".format(self.color)
    
    def __hash__(self):
        return 1 if self.color == 'white' else 0
    
    def opposite(self):
        return 'black' if self.color == 'white' else 'white'
__all__.append('Side')

class Player (object):
    
    isFrozen = False
    total_moves = 0
    
    def __init__(self, color):
        
        self.color = Side(color)
        self.score = 0
        self.remaining_pieces = 16
        self.pawns = 8
        self.knights = 2
        self.rooks = 2
        self.bishops = 2
        self.kings = 1
        self.queens = 1
        self.board = None  # will be changed later
        self.moves = 0
        self.owned_pieces = set()
        
        self._uuid = uuid.uuid4()
        
    def __repr__(self):
        return "Player('{}')".format(self.color.color)
    
    def _update(self):
        self.remaining_pieces = (self.pawns +
                                 self.knights +
                                 self.rooks +
                                 self.bishops +
                                 self.kings +
                                 self.queens)
    
    @call_trace(5)
    def is_turn(self):
        return self.color == self.board.turn
    
    def add_owned_piece(self, p):
        wasfrozen = False
        if self.isFrozen:
            wasfrozen = True
            self.unfreeze()
        self.owned_pieces.add(p)
        self._update()
        if wasfrozen:
            self.freeze()
        
    def freeze(self):
        self.isFrozen = True
        self.owned_pieces = list(self.owned_pieces)
    
    def unfreeze(self):
        self.isFrozen = False
        self.owned_pieces = set(self.owned_pieces)
    
    def premove(self):
        if not self.is_turn():
            return
        else:
            self.freeze()
            self._update()
    
    def postmove(self):
        self.unfreeze()
        self._update()
        self.moves += 1
        self.total_moves += 1
    
    def set_board(self, board):
        self.board = board
    
    def lose_piece(self, piece):
        self.freeze()
        if piece.ptype == 'pawn':
            self.pawns -= 1
        elif piece.ptype == 'knight':
            self.knights -= 1
        elif piece.ptype == 'rook':
            self.rooks -= 1
        elif piece.ptype == 'bishop':
            self.bishops -= 1
        elif piece.ptype == 'king':
            self.kings -= 1
        elif piece.ptype == 'queen':
            self.queens -= 1
        self._update()
        self.unfreeze()
    
    @call_trace(2)
    def validatemove(self, p1, p2):
        piece = self.board[p1]
        turn = self.is_turn()
        allowed = piece.apply_ruleset(p2)
        path = piece.path_to(p2)
        path_check = piece.check_path(path)
        if self.board.cfg.do_checkmate:
            check = not self.board.will_checkmate(p1, p2)
        else:
            check = True
        log_msg('validatemove: piece={}, turn={}, allowed={}, path={}, path_check={}, check={}'.format(
                               piece,    turn,    allowed,    path,    path_check,    check), 3)
        return turn and allowed and path_check and check
    
    def make_move(self, p1, p2):
        self.board.freeze()
        piece = self.board[p1]
        piece.coord = p2
        self.board.unfreeze()
__all__.append('Player')

