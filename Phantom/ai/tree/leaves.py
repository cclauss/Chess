# -*- coding: utf-8 -*-

"""Tree nodes & leaves."""

from Phantom.ai.pos_eval.basic import pos_eval_basic
from Phantom.ai.pos_eval.advanced import pos_eval_advanced
from Phantom.ai.settings import window, maxdepth
from Phantom.core.board import Board
import uuid

class Node (object):
    
    cnum = 0
    spawndepth = 0
    used_layouts = set()
    
    def __init__(self, depth, terminal, board):
        self.depth = depth
        self.is_terminal = terminal or (self.depth >= maxdepth)
        self.board = Board(fen=board.fen_str())  # deepcopy the board
        self.score = pos_eval_advanced(self.board)
        self.nid = self.cnum + 1
        if self.nid >= window:
            self.spawndepth += 1
        self.cnum = self.nid
        self._uuid = uuid.uuid4()
        self.parent = None
        self.children = []
        self.tree = None
    
    def __hash__(self):
        return self.depth * self.board.__hash__()
    
    def set_tree(self, t):
        self.tree = t
        self.tree.used_layouts.append(self.board.fen_str())
    
    def set_parent(self, p):
        self.parent = p
        self.parent.set_child(self)
    
    def set_child(self, c):
        self.children.append(c)
    
    def variate(self, *args):
        fen = self.board.fen_str()
        self.board.move(*args)
        ret = Board(fen=self.board.fen_str())
        self.board = Board(fen=fen)
        return ret

