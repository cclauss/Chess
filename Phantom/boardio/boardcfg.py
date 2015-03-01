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

"""A package of user settings to go with a game.

This file is 1-level import clean.
"""

from Phantom.constants import use_unicode

class Cfg (object):
    
    def __init__(self, **kwargs):
        self.highlight = kwargs.get('highlight', True)
        self.force_moves = kwargs.get('force_moves', False)
        self.disp_coords = kwargs.get('disp_coords', False)
        self.coord_mode = kwargs.get('coord_mode', 'chess')
        self.move_limit = kwargs.get('move_limit', 50)
        self.disp_sqrs = kwargs.get('disp_sqrs', True)
        self.disp_pieces = kwargs.get('disp_pieces', True)
        self.do_checkmate = kwargs.get('do_checkmate', False)
        self.use_unicode = kwargs.get('use_unicode', use_unicode)
        self.board = None
        self.game = None
    
    def set_board(self, b):
        self.board = b
        if hasattr(self.board, 'game'):
            self.game = self.board.game

    def set_game(self, g):
        self.game = g

# A quick & dirty class to prevent polluting the globals
# Usage would be as a 'data' or similar attribute:
# self.data = Namespace()
# then to set/get variables:
# self.data.x = 5; print self.data.x
class Namespace (object): 
    
    def __getitem__(self, i):
        if hasattr(self, i):
            return getattr(self, i)
        else:
            return None
    
    def __setitem__(self, i, val):
        setattr(self, i, val)

