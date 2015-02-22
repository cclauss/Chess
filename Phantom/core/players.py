# -*- coding: utf-8 -*-

"""Player class."""

from Phantom.constants import *
from Phantom.core.exceptions import InvalidMove, LogicError
from Phantom.core.coord.point import Coord
from Phantom.functions import round_down, dist
import uuid

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
            raise LogicError("Couldn't identify color: {}".format(color))
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
    def is_turn(self):
        return self.color == self.board.turn
    
    def add_owned_piece(self, p):
        self.owned_pieces.add(p)
        self._update()
        
    def freeze(self):
        self.isFrozen = True
        self.owned_pieces = frozenset(self.owned_pieces)
    
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
        return turn and allowed and path_check and check
    
    def make_move(self, p1, p2):
        self.board.freeze()
        piece = self.board[p1]
        piece.coord = p2
        if piece.ptype == 'pawn' and piece.firstmove:
            if round_down(dist(p1, p2)) == 2:
                y = abs(p2.y - p1.y) / 2
                pos = Coord(p1.x, y)
                self.board.en_passant_rights = pos.as_chess()
        self.board.unfreeze()

