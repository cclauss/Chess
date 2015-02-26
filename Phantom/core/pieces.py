# -*- coding: utf-8 -*-

"""The core of the pieces."""

from Phantom.constants import *
from Phantom.core.coord import Coord, Grid, bounds
from Phantom.core.exceptions import InvalidMove, InvalidDimension
from Phantom.core.coord.vectored_lists import *
from Phantom.core.coord.dirs import dirfinder
from Phantom.core.players import Side
from Phantom.boardio.boardcfg import Namespace
from Phantom.functions import dist, round_up, round_down
from Phantom.utils.debug import call_trace, log_msg
import uuid

class ChessPiece (object):
    
    allIsFrozen = False  # all piece level freeze
    bounds = bounds
    
    # overwritten by subclasses
    ptype = None
    default_origins = []
    
    def __init__(self, pos, color, owner=None):
        self.color = Side(color)
        if not pos in self.bounds:
            raise InvalidDimension('Piece spawned out of bounds: {}'.format(str(pos)), 
                                   'Phantom.core.pieces.ChessPiece.__init__()')
        self.coord = pos
        self.isFrozen = False  # piece level freeze
        self.promotable = False
        self.firstmove = True
        self._uuid = uuid.uuid4()
        self.fen_char = eval('c_{}_{}'.format(self.color.color, self.ptype))
        if use_unicode:
            self.disp_char = eval('d_{}_{}'.format(self.color.color, self.ptype))
        else:
            self.disp_char = self.fen_char
        self.pythonista_gui_imgname = 'Chess set images {} {}.jpg'.format(self.color.color, self.ptype)
        if owner:
            self.owner = None  # Set the attribute before it can be checked in set_owner()
            self.set_owner(owner)
        else:
            self.owner = None
    
    def __repr__(self):
        return '<{} at {} in {}>'.format(self.ptype, self.coord, hex(id(self)))
    
    def __hash__(self):
        return int(self._uuid) % (self.owner.moves + 1)
    
    def set_owner(self, owner):
        if self.owner is not None:
            return
        self.owner = owner
        self.owner.add_owned_piece(self)
    
    # This applies the piece's ruleset as described in level 1.1
    def apply_ruleset(self, target):
        return True
    
    # method is only usable after set_owner is used
    def suicide(self):
        self.owner.board.kill(self)
    
    @property
    def image(self):
        return '{}_{}'.format(self.color, self.ptype)
    
    # implementation detail 5
    @call_trace(3)
    def valid(self):
        ret = []
        for tile in self.owner.board.tiles:
            if self.owner.validatemove(self.coord, tile.coord):
                ret.append(tile.coord)
        return ret
    
    @property
    def is_promotable(self):
        if self.ptype == 'pawn':
            if self.color == 'white':
                if self.coord.y == 7:
                    return True
            if self.color == 'black':
                if self.coord.y == 0:
                    return True
        return False
    
    @call_trace(3)
    def check_target(self, target):
        piece = self.owner.board[target]
        if (piece == []) or (piece is None):
            return True
        elif piece.color == self.color:
            return False
        else:
            return True
    
    @call_trace(3)
    def check_path(self, path):
        for pos in path[:-1]:
            piece = self.owner.board[pos]
            if not ((piece == []) or (piece is None)):
                return False
        return True

    @call_trace(3)
    def path_to(self, target):
        start = self.coord
        end = target
        dir = dirfinder(self, target)
        dist_to = round_down(dist(self.coord, target))
        path = dir[1](self)
        squares = path[:dist_to]
        return squares
    
    @call_trace(2)
    def is_move_valid(self, target):
        does_follow_rules = self.apply_ruleset(target)
        is_valid_target = self.check_target(target)
        path = self.path_to(target)
        is_clear_path = self.check_path(path)
        is_turn = self.owner.is_turn()
        return does_follow_rules and is_valid_target and is_clear_path and is_turn
    
    @staticmethod
    def type_from_chr(chr):
        if chr in ('p', 'P'):
            return Pawn
        elif chr in ('r', 'R'):
            return Rook
        elif chr in ('n', 'N'):
            return Knight
        elif chr in ('b', 'B'):
            return Bishop
        elif chr in ('k', 'K'):
            return King
        elif chr in ('q', 'Q'):
            return Queen

# Individual piece subtypes

class Pawn (ChessPiece):
    
    ptype = 'pawn'
    default_origins = [Coord(x, y) for x in range(grid_width) for y in (1, 6)]
    
    @call_trace(4)
    def apply_ruleset(self, target):
        
        if self.color == 'white':
            allowed = [Coord(self.coord.x, self.coord.y+1)]
            if self.firstmove:
                allowed.append(Coord(self.coord.x, self.coord.y+2))
            tests = [Coord(self.coord.x+1, self.coord.y+1),
                     Coord(self.coord.x-1, self.coord.y+1)]
            for test in tests:
                if self.owner.board[test] is not None:
                    allowed.append(test)
            
        elif self.color == 'black':
            allowed = [Coord(self.coord.x, self.coord.y-1)]
            if self.firstmove:
                allowed.append(Coord(self.coord.x, self.coord.y-2))
            tests = [Coord(self.coord.x+1, self.coord.y-1),
                     Coord(self.coord.x-1, self.coord.y-1)]
            for test in tests:
                if self.owner.board[test] is not None:
                    allowed.append(test)
            
        return target in allowed


class Rook (ChessPiece):
    
    ptype = 'rook'
    default_origins = [Coord(x, y) for x in (0, 7) for y in (0, 7)]
    
    @call_trace(4)
    def apply_ruleset(self, target):
        allowed = []
        allowed.extend(north(self))
        allowed.extend(south(self))
        allowed.extend(east(self))
        allowed.extend(west(self))
        return target in allowed

class Bishop (ChessPiece):
    
    ptype = 'bishop'
    default_origins = [Coord(x, y) for x in (2, 5) for y in (0, 7)]
    
    @call_trace(4)
    def apply_ruleset(self, target):
        allowed = []
        allowed.extend(ne(self))
        allowed.extend(nw(self))
        allowed.extend(se(self))
        allowed.extend(sw(self))
        return target in allowed

class Queen (ChessPiece):
    
    ptype = 'queen'
    default_origins = [Coord(3, y) for y in (0, 7)]
    
    @call_trace(4)
    def apply_ruleset(self, target):
        allowed = []
        allowed.extend(north(self))
        allowed.extend(south(self))
        allowed.extend(east(self))
        allowed.extend(west(self))
        allowed.extend(ne(self))
        allowed.extend(nw(self))
        allowed.extend(se(self))
        allowed.extend(sw(self))
        return target in allowed

class King (ChessPiece):
    
    ptype = 'king'
    default_origins = [Coord(4, y) for y in (0, 7)]
    
    @call_trace(4)
    def _apply_ruleset(self, target):
        if round_down(dist(self.coord, target)) == 1:
            return True
        return False

    @call_trace(4)
    def apply_ruleset(self, target):
        if not self.owner.board.cfg.do_checkmate:
            return self._apply_ruleset(target)
        empty_board = self._apply_ruleset(target)  # could move if there were no pieces on the board
        other_allowed = []
        self.owner.board.set_checkmate_validation(False)  # avoid recursion
        for piece in self.owner.board.pieces:
            if piece is self:
                continue
            else:
                other_allowed.extend(piece.valid)
        self.owner.board.set_checkmate_validation(True)
        if self.coord in other_allowed:
            return False
        else:
            return empty_board

class Knight (ChessPiece):
    
    ptype = 'knight'
    default_origins = [Coord(x, y) for x in (1, 6) for y in (0, 7)]
    
    @call_trace(4)
    def apply_ruleset(self, target):
        allowed = [self.coord + Coord(1, 2),
                   self.coord + Coord(2, 1),
                   self.coord + Coord(2, -1),
                   self.coord + Coord(1, -2),
                   self.coord - Coord(1, 2),
                   self.coord - Coord(2, 1),
                   self.coord - Coord(2, -1),
                   self.coord - Coord(1, -2)]
        return target in allowed
    
    @call_trace(4)
    def path_to(self, target):
        return [0]

