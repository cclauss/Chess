# -*- coding: utf-8 -*-

"""The main screen."""

from scene import *
from Phantom.core.coord.point import Coord, bounds
from Phantom.utils.debug import log_msg, call_trace
from Phantom.constants import *
import sys

class ChessMainScreen (Scene):
    
    def __init__(self, game, main=None):
        self.game = game
        self.tmp_t = 0
        self.parent = main  # Phantom.gui_pythonista.main_scene.MultiScene object
    
    def setup(self):
        self.highlight = self.game.board.cfg.highlight
        self.coord_disp_mode = {'onoff': self.game.board.cfg.disp_coords,
                                'mode': self.game.board.cfg.coord_mode}
        self.is_selected = False
        self.selected = Coord(None, None)
        self.target = self.selected
        self.err = None
        import os
        folder = 'imgs'
        format = 'Chess set images {} {}.jpg'

        files = [os.path.join(folder, format.format(color, type))
                 for type in ('pawn', 'rook', 'queen', 'king', 'bishop', 'knight')
                 for color in ('black', 'white')]

        img_names = {}
        for file in files:
            name = os.path.split(file)[1]
            img = scene.load_image_file(file)
            img_names.update({name: img})
        self.img_names = img_names
    
    def did_err(self, e):
        self.err = sys.exc_info()
        self.selected = Coord(None, None)
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
                    self.selected = Coord(None, None)
            else:
                self.target = cpos
                try:
                    self.game.board.move(self.selected, self.target)
                except Exception as e:
                    self.did_err(e)
    
    def draw(self):
        background(0, 0, 0)
        fill(1, 1, 1, 1)
        for piece in self.game.board.pieces:
            tint(1, 1, 1, 0.5)
            pos = piece.coord.as_screen()
            img = self.img_names[piece.pythonista_gui_imgname]
            image(img, pos.x, pos.y, scale_factor, scale_factor)
            tint(1, 1, 1, 1)
            if piece.coord == self.selected:
                fill(0.8, 1, 0.8, 0.3)
                rect(pos.x, pos.y, scale_factor, scale_factor)
                fill(1, 1, 1, 1)
        for tile in self.game.board.tiles:
            
            # this returns either (0.27462, 0.26326, 0.27367) if the piece is white
            # or (0.86174, 0.85795, 0.85417) if the piece is black
            color = tile.color.tilecolor
            color += (0.3,)  # alpha value
            
            # get the position of the tile in screen coords
            # this method DOES function correctly as shown by the above `for piece in pieces` loop
            pos = tile.coord.as_screen()
            
            # draw
            fill(*color)
            rect(pos.x, pos.y, scale_factor, scale_factor)
            fill(1, 1, 1, 1)
        

if __name__ == '__main__':
    from Phantom.core.game_class import ChessGame
    s = ChessMainScreen(ChessGame())
    run(s)

