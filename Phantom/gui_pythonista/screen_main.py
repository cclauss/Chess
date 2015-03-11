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

"""The main screen."""

from scene import *
from Phantom.core.coord.point import Coord, bounds
from Phantom.core.chessobj import PhantomObj
from Phantom.utils.debug import log_msg, call_trace
from Phantom.constants import *
from Phantom.ai.pos_eval.advanced import pos_eval_advanced
from Phantom.core.exceptions import InvalidMove
import sys

class ChessMainScreen (Scene, PhantomObj):
    
    def __init__(self, game, main=None):
        self.game = game
        self.tmp_t = 0
        self.parent = main  # Phantom.gui_pythonista.main_scene.MultiScene object
        if self.parent is not None:
            self.parent.set_main_scene(self)
    
    def setup(self):
        self.coord_disp_mode = {'onoff': self.game.board.cfg.disp_coords,
                                'mode': self.game.board.cfg.coord_mode}
        self.render_mode = {'sqrs': self.game.board.cfg.disp_sqrs,
                            'pieces': self.game.board.cfg.disp_pieces,
                            'valid': self.game.board.cfg.highlight,
                            'coords': self.game.board.cfg.disp_coords,
                            'turn': self.game.board.cfg.disp_turn,
                            'timers': self.game.board.cfg.disp_timers}
        self.is_selected = False
        self.selected = Coord(None, None)
        self.target = self.selected
        self.err = None
        self.err_pos = Coord(None, None)
        self.valid_cache = []
        import os
        folder = 'imgs'
        format = 'Chess set images {} {}.jpg'

        files = [os.path.join(phantom_dir, 'gui_pythonista', folder, format.format(color, type))
                 for type in ('pawn', 'rook', 'queen', 'king', 'bishop', 'knight')
                 for color in ('black', 'white')]

        img_names = {}
        for file in files:
            name = os.path.split(file)[1]
            img = load_image_file(file)
            img_names.update({name: img})
        self.img_names = img_names
        self.turn_indicator_img = 'White_Square'
        self.pos_score = None
        self.disp_score = False
        min = Coord(0, 0).as_screen()
        max = Coord(8, 8).as_screen()
        self.bounds = Rect(min.x, min.y, max.x-min.x, max.y-min.y)
        self.size = screen_size
        self.won = self.game.is_won()
    
    def set_parent(self, p):
        self.parent = p
        self.parent.set_main_scene(self)
    
    def did_err(self, e):
        self.err = sys.exc_info()
        self.selected = Coord(None, None)
        self.is_selected = False
        self.game.board.freeze()
    
    def touch_began(self, touch):
        self.valid_cache = []
        tpos = Coord(touch.location.x, touch.location.y)
        cpos = Coord.from_screen(tpos)
        if touch.location in self.bounds:
            if not self.is_selected:
                piece = self.game.board[cpos]
                if isinstance(piece, list):
                    try:
                        raise ChessError('More than one piece at position', 
                                         'Phantom.gui_pythonista.screen_main.ChessMainScreen.touch_began()')
                    except ChessError as e:
                        self.did_err(e)
                        return
                if piece is not None:
                    self.selected = cpos
                    self.valid_cache = piece.valid()
                    self.is_selected = True
                else:
                    self.selected = Coord(None, None)
            else:
                self.target = cpos
                try:
                    if self.game.board[self.selected].ptype == 'king':
                        piece = self.game.board[self.selected]
                        if piece.color == 'white':
                            if self.target == Coord(6, 0):
                                if 'K' in self.game.board.castling_rights:
                                    self.game.castle('K')
                            elif self.target == Coord(2, 0):
                                if 'Q' in self.game.board.castling_rights:
                                    self.game.castle('Q')
                        elif piece.color == 'black':
                            if self.target == Coord(6, 7):
                                if 'k' in self.game.board.castling_rights:
                                    self.game.castle('k')
                            elif self.target == Coord(2, 7):
                                if 'q' in self.game.board.castling_rights:
                                    self.game.castle('q')
                    self.game.move(self.selected, self.target)
                    self.disp_score = False
                    self.won = self.game.is_won()
                except InvalidMove as e:
                    self.err_pos = self.target
                    self.did_err(e)
                except Exception as e:
                    self.did_err(e)
                self.selected = Coord(None, None)
                self.target = Coord(None, None)
                self.is_selected = False
        else:
            if 0 < touch.location.x <= scale_factor and 6*scale_factor < touch.location.y <= 7*scale_factor:
                self.parent.switch_scene(self.game.data['screen_options'])
            if 0 < touch.location.x <= scale_factor and 5*scale_factor < touch.location.y <= 6*scale_factor:
                self.game.ai_easy()
            if 0 < touch.location.x <= scale_factor and 4*scale_factor < touch.location.y <= 5*scale_factor:
                self.game.ai_hard()
            if 0 < touch.location.x <= scale_factor and 3*scale_factor < touch.location.y <= 4*scale_factor:
                self.pos_score = pos_eval_advanced(self.game.board)
                self.disp_score = True
            if 0 < touch.location.x <= scale_factor and 2*scale_factor < touch.location.y <= 3*scale_factor:
                self.game.rollback()
            if 0 < touch.location.x <= scale_factor and scale_factor < touch.location.y <= 2*scale_factor:
                self.is_selected = False
                self.selected = Coord(None, None)
                self.target = Coord(None, None)
    
    def draw(self):
        background(0, 0, 0)
        fill(1, 1, 1, 1)
        if self.render_mode['pieces']:
            for piece in self.game.board.pieces:
                tint(1, 1, 1, 0.5)
                pos = piece.coord.as_screen()
                img = self.img_names[piece.pythonista_gui_imgname]
                image(img, pos.x, pos.y, scale_factor, scale_factor)
                tint(1, 1, 1, 1)
                if piece.coord == self.selected:
                    fill(0.23347,0.3564,0.59917, 0.6)
                    rect(pos.x, pos.y, scale_factor, scale_factor)
                    fill(1, 1, 1, 1)
            if self.render_mode['timers']:
                white = str(self.game.board.player1.timer.get_run())
                black = str(self.game.board.player2.timer.get_run())
                bpos = Coord(992, 672)
                wpos = Coord(992, 96)
                tint(1, 1, 1, 1)
                text(black, x=bpos.x, y=bpos.y)
                text(white, x=wpos.x, y=wpos.y)
                tint(1, 1, 1, 1)
        if self.render_mode['sqrs']:
            for tile in self.game.board.tiles:
                color = tile.color.tilecolor
                color += (0.57,)  # alpha value
                pos = tile.coord.as_screen()
                fill(*color)
                rect(pos.x, pos.y, scale_factor, scale_factor)
                fill(1, 1, 1, 1)
                if self.render_mode['coords']:
                    center = Coord(pos.x + (scale_factor / 2), pos.y + (scale_factor / 2))
                    chess_pos = center + Coord(0, 10)
                    coord_pos = center - Coord(0, 10)
                    chess = tile.coord.as_chess()
                    coord = str(tile.coord.as_tup())
                    text(chess, x=chess_pos.x, y=chess_pos.y)
                    text(coord, x=coord_pos.x, y=coord_pos.y)
            if self.err_pos.x is not None:
                sc = self.err_pos.as_screen()
                fill(1, 0, 0, 0.3)
                rect(sc.x, sc.y, scale_factor, scale_factor)
                fill(1, 1, 1, 1)
                tint(0, 0, 1, 1)
                text('Move\nInvalid', x=(sc.x + scale_factor/2), y=(sc.y + scale_factor/2))
                tint(1, 1, 1, 1)
        if self.render_mode['valid']:
            for tile in self.game.board.tiles:
                if tile.coord in self.valid_cache:
                    pos = tile.coord.as_screen()
                    fill(0.47934,0.81198,0.41839, 0.3)
                    rect(pos.x, pos.y, scale_factor, scale_factor)
                    fill(1, 1, 1, 1) 
        if self.render_mode['turn']:
            if self.game.board.turn == 'white':
                turn_y = 1 * scale_factor
            elif self.game.board.turn == 'black':
                turn_y = 7 * scale_factor
            pos = Coord(896, turn_y)
            size = Coord(scale_factor / 2, scale_factor / 2)
            tint(1, 1, 1, 1)
            image(self.turn_indicator_img, pos.x, pos.y, size.x, size.y)
            tint(1, 1, 1, 1)
        if self.won:
            pos = Coord(self.size.w/2, self.size.h/2)
            tint(0.32645,0.28306,0.93492)
            # commented out until the bug in ChessGame.is_won() is fixed to be 
            # less annoying
            text('{} wins'.format(self.won), x=pos.x, y=pos.y, font_size=40.0)
            tint(1, 1, 1, 1)
        
        # Buttons
        text('AI Easy', x=scale_factor/2, y=scale_factor*6 - scale_factor/2)
        text('AI Hard', x=scale_factor/2, y=scale_factor*5 - scale_factor/2)
        text('Get score', x=scale_factor/2, y=scale_factor*4 - scale_factor/2)
        if self.disp_score:
            text(str(self.pos_score), x=scale_factor/2, y=scale_factor*4 - scale_factor/1.5)
        text('Undo', x=scale_factor/2, y=scale_factor*3 - scale_factor/2)
        text('Deselect', x=scale_factor/2, y=scale_factor*2 - scale_factor/2)
        text('Options', x=scale_factor/2, y=scale_factor*7 - scale_factor/2)

if __name__ == '__main__':
    from Phantom.core.game_class import ChessGame, loadgame
    game = ChessGame() #loadgame('Long Endgame 1')
    game.board.cfg.disp_sqrs = True
    s = ChessMainScreen(game)
    run(s)

