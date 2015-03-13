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

"""The screen that allows users to select a piece to promote a pawn to."""

from scene import *
from Phantom.core.game_class import ChessGame
from Phantom.core.pieces import Rook, Bishop, Knight, Queen
from Phantom.core.coord.point import Coord
from Phantom.core.chessobj import PhantomObj
from Phantom.constants import phantom_dir, scale_factor, screen_width, screen_height
import os

class ChessPromoteScreen (Scene, PhantomObj):
    
    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent
        if self.parent is not None:
            self.parent.set_promote_scene(self)
    
    def setup(self):
        # Determine which pawn is being promoted and set up the options
        self.turn = self.game.board.turn
        for p in self.game.board.pieces:
            if p.is_promotable:
                self.promoter = p
                self.color = p.color
        if not hasattr(self, 'promoter'):
            self.parent.switch_scene(self.game.data['screen_main'])
        self.owner = self.promoter.owner
        y = 7 if p.color == 'white' else 0
        self.spawncoord = Coord(self.promoter.coord.x, y)
        qpos, rpos, bpos, kpos = [Coord(i*scale_factor + (screen_width/2 - 2*scale_factor), 
                                        screen_height/2) for i in range(4)]
        self.queen = Queen(qpos, self.color, self.promoter.owner)
        self.rook = Rook(rpos, self.color, self.promoter.owner)
        self.bishop = Bishop(bpos, self.color, self.promoter.owner)
        self.knight = Knight(kpos, self.color, self.promoter.owner)
        self.pieces = [self.queen, self.rook, self.bishop, self.knight]
        self.selected = None
        
        files = [p.pythonista_gui_imgname for p in self.pieces]
        readfiles = [os.path.join(phantom_dir, 'gui_pythonista', 'imgs', f) for f in files]

        img_names = {}
        for file in readfiles:
            name = os.path.split(file)[1]
            img = load_image_file(file)
            img_names.update({name: img})
        self.img_names = img_names
    
    def set_parent(self, s):
        self.parent = s
        self.parent.set_promote_scene(self)
    
    def touch_began(self, touch):
        qrect = Rect(self.queen.coord.x, self.queen.coord.y, scale_factor, scale_factor)
        rrect = Rect(self.rook.coord.x, self.rook.coord.y, scale_factor, scale_factor)
        brect = Rect(self.bishop.coord.x, self.bishop.coord.y, scale_factor, scale_factor)
        krect = Rect(self.knight.coord.x, self.knight.coord.y, scale_factor, scale_factor)
        
        if touch.location in qrect:
            self.selected = self.queen
        elif touch.location in rrect:
            self.selected = self.rook
        elif touch.location in brect:
            self.selected = self.bishop
        elif touch.location in krect:
            self.selected = self.knight
        
        if self.selected:
            self.promote()
            self.parent.switch_scene(self.game.data['screen_main'])
        
    def promote(self):
        newpiece = self.selected
        oldpiece = self.promoter
        self.game.board.kill(oldpiece)
        self.game.board.pieces.add(newpiece)

    def draw(self):
        background(0, 0, 0)
        for i, piece in enumerate(self.pieces):
            img = self.img_names[piece.pythonista_gui_imgname]
            x = i*scale_factor + (screen_width/2 - 2*scale_factor)  # center the images
            y = screen_height/2
            image(img, x, y, scale_factor, scale_factor)
        tpos = Coord(screen_width/2, screen_height/2 + 2*scale_factor)
        text('Select a piece to promote to', x=tpos.x, y=tpos.y)

if __name__ == '__main__':
    import Phantom as P
    g = ChessGame('Long Endgame 1')
    g.board.pieces.add(P.Pawn(P.Coord(0, 1), 'black', g.board.player2))
    g.gui()

