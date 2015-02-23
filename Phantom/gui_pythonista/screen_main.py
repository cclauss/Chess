# -*- coding: utf-8 -*-

"""The main screen."""

from scene import *
from Phantom.core.coord.point import Coord, bounds
from Phantom.core.game_class import ChessGame
from Phantom.constants import *
import sys

class ChessMainScreen (Scene):
    
    def __init__(self, game):
        self.game = game
        self.tmp_t = 0
    
    def setup(self):
        self.highlight = self.game.board.cfg.highlight
        self.coord_disp_mode = {'onoff': self.game.board.cfg.disp_coords,
                                'mode': self.game.board.cfg.coord_mode}
        self.is_selected = False
        self.selected = Coord(float('nan'), float('nan'))
        self.target = self.selected
        self.err = None
        from Phantom.gui_pythonista.sprites import img_names
        self.img_names = img_names
    
    def did_err(self, e):
        self.err = sys.exc_info()
        self.selected = Coord(float('nan'), float('nan'))
        self.is_selected = False
        self.game.board.freeze()
    
    def touch_began(self, touch):
        tpos = Coord(touch.location.x, touch.location.y)
        cpos = Coord.from_screen(tpos)
        if cpos in bounds:
            if not self.selected:
                piece = self.game.board[cpos]
                if piece is not None:
                    self.selected = cpos
                else:
                    self.selected = Coord(float('nan'), float('nan'))
            else:
                self.target = cpos
                try:
                    self.game.board.move(self.selected, self.target)
                except Exception as e:
                    self.did_err(e)
    
    def draw(self):
        background(0, 0, 0)
        fill(1, 1, 1)
        for piece in self.game.board.pieces:
            pos = piece.coord.as_screen()
            img = self.img_names[piece.pythonista_gui_imgname]
            image(img, pos.x, pos.y, scale_factor, scale_factor)
        for tile in self.game.board.tiles:
            color = tile.color.tilecolor
            pos = piece.coord.as_screen()
            fill(*color)
            rect(scale_factor, scale_factor, pos.x, pos.y)
            fill(1, 1, 1)
        

run(ChessMainScreen(ChessGame()))

