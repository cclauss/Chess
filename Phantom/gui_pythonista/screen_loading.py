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

"""A loading screen."""

from scene import *
from Phantom.constants import debug, screen_width, screen_height, version
from Phantom.utils.lic import short

class ChessLoadingScreen (Scene):
    
    def __init__(self, main=None):
        self.parent = main
        if self.parent is not None:
            self.parent.set_load_scene(self)
        self.tmp_t = 0
    
    def setup(self):
        pass
    
    def touch_began(self, touch):
        self.parent.did_begin()
    
    def draw(self):
        background(0, 0, 0)
        fill(1, 1, 1)
        x = screen_width / 2
        s_y = screen_height / 2 + 100
        d_y = s_y - 30
        l_y = d_y - 75
        tint(0.32645,0.28306,0.93492)
        text('PhantomChess version {}'.format(version), x=x, y=s_y, font_size=20.0)
        tint(1, 1, 1)
        if debug:
            text('Debugger set to level {}'.format(debug), x=x, y=d_y)
        for i, line in enumerate(short().splitlines()):
            text(line, x=x, y=l_y - (i*20))

if __name__ == '__main__':
    run(ChessLoadingScreen())

