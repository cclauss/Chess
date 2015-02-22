# -*- coding: utf-8 -*-

"""A package of user settings to go with a game."""

class Cfg (object):
    
    def __init__(self, **kwargs):
        self.highlight = kwargs.get('highlight', True)
        self.force_moves = kwargs.get('force_moves', False)
        self.disp_coords = kwargs.get('disp_coords', False)
        self.coord_mode = kwargs.get('coord_mode', 'chess')
        self.move_limit = kwargs.get('move_limit', 50)
        self.disp_sqrs = kwargs.get('disp_sqrs', True)
        self.do_checkmate = kwargs.get('do_checkmate', True)
        self.board = None
        self.game = None
    
    def set_board(self, b):
        self.board = b
        if hasattr(self.board, 'game'):
            self.game = self.board.game

    def set_game(self, g):
        self.game = g

