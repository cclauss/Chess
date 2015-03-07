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

"""Options screen."""

from scene import *
from Phantom.boardio.boardcfg import Namespace, Cfg
from Phantom.core.chessobj import PhantomObj
from Phantom.constants import scale_factor, screen_size
from Phantom.core.coord.point import Coord

class ChessOptionsScreen (Scene, PhantomObj):
    
    def __init__(self, game, main=None):
        self.tmp_t = 0
        
        self.game = game
        self.parent = main
        if self.parent is not None:
            self.parent.set_options_scene(self)
        self.data = Cfg()
    
    def setup(self):
        self.game.data['has_gui'] = True
        self.data['game'] = self.game
        self.data.copy_data_from(self.game.board.cfg)
        
                      # (name,           display name,     show value,     position,               action)
        self.buttons = [('disp_coords',  'Show coords',       True,     Coord(0, 672),       self.tog_disp_coords),
                        ('',             'Save & exit',       'NA',     Coord(930, 576),     self.return_to_game),
                        ('force_moves',  'Force moves',       True,     Coord(0, 576),       self.tog_force_moves),
                        ('disp_turn',    'Show turn',         True,     Coord(0, 480),       self.tog_disp_turn),
                        ('highlight',    'Show valid',        True,     Coord(0, 384),       self.tog_highlight),]
        self.button_size = Coord(scale_factor, scale_factor)
        self.size = screen_size
    
    # ------------------- Button actions ---------------------
    def tog_disp_coords(self):
        self.data['disp_coords'] = not self.data['disp_coords']
    
    def return_to_game(self):
        self.parent.switch_scene(self.game.data['screen_main'])
    
    def tog_force_moves(self):
        self.data['force_moves'] = not self.data['force_moves']
    
    def tog_disp_turn(self):
        self.data['disp_turn'] = not self.data['disp_turn']
    
    def tog_highlight(self):
        self.data['highlight'] = not self.data['highlight']
    # ------------------ End button actions ------------------
    
    def set_parent(self, p):
        self.parent = p
    
    def sync_data(self):
        # update game data first to push any changes
        self.game.data.copy_data_from(self.data)
        
        # update our data as well in case any new variables have
        # been set
        self.data.copy_data_from(self.game.board.cfg)

    def draw_toggle(self, name, curval, pos):
        name = str(name)
        val = str(curval)
        x, y = pos.x, pos.y
        w = h = scale_factor
        mid = Coord(x + (w / 2), y + (h / 2))
        label = Coord(mid.x, mid.y + 10)
        state = Coord(mid.x, mid.y - 10)
        text(name, x=label.x, y=label.y)
        text(val, x=state.x, y=state.y)
    
    def draw_button(self, name, pos):
        name = str(name)
        x, y = pos.x, pos.y
        w = h = scale_factor
        mid = Coord(x + (w / 2), y + (h / 2))
        text(name, x=mid.x, y=mid.y)
    
    def touch_began(self, touch):
        for button in self.buttons:
            hit_test = Rect(button[3].x, button[3].y, self.button_size.x, self.button_size.y)
            if touch.location in hit_test:
                button[4]()
                self.sync_data()
    
    def draw(self):
        background(0, 0, 0)
        
        for b in self.buttons:
            # use '== True' here to avoid catching values like "NA"
            if b[2] == True:
                self.draw_toggle(b[1], self.data[b[0]], b[3])
            elif b[2] in (False, 'NA'):
                self.draw_button(b[1], b[3])
                

if __name__ == '__main__':
    from Phantom.core.game_class import ChessGame
    g = ChessGame()
    s = ChessOptionsScreen(g)
    run(s)

