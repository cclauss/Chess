# -*- coding: utf-8 -*-

"""A loading screen."""

from scene import *
from Phantom.constants import debug, screen_width, screen_height, version

class ChessLoadingScreen (Scene):
    
    def __init__(self, main=None):
        self.parent = main
        self.tmp_t = 0
    
    def setup(self):
        pass
    
    def touch_began(self, touch):
        self.parent.did_begin()
    
    def draw(self):
        background(0, 0, 0)
        fill(1, 1, 1)
        text('PhantomChess version {}'.format(version), x=screen_width/2, y=screen_height/2)
        if debug:
            text('Debugger set to level {}'.format(debug), x=screen_width/2, y=(screen_height/2)-20)

if __name__ == '__main__':
    run(ChessLoadingScreen())

