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

"""The class that holds a complete game of Chess.

Generally, use this class rather than Phantom.core.board.Board, because this class
keeps track of history, which Board doesn't."""

from Phantom.core.board import Board, Tile, load as _loadboard
from Phantom.core.players import Player, Side
from Phantom.core.pieces import ChessPiece, Pawn, Rook, Knight, Bishop, King, Queen
from Phantom.core.exceptions import ChessError, LogicError, InvalidMove, InvalidDimension
from Phantom.core.coord import *
from Phantom.boardio.boardcfg import Cfg, Namespace
from Phantom.boardio.load import listgames

__all__ = []

def loadgame(name):
    board = _loadboard(name)
    return CessGame(board)

class ChessGame (object):
    
    def __init__(self, *args, **kwargs):
        self.board = Board()
        self.player1 = self.board.player1
        self.player2 = self.board.player2
        
        if len(args) > 0:
            if isinstance(args[0], str):
                # assume name of a game and load it
                self.board = _loadboard(args[0])
        
        for arg in args:
            if isinstance(arg, Board):
                self.board = arg
            if isinstance(arg, Player):
                self.player1 = arg
                self.player2 = args[args.index(arg)+1]
        
        self.board.set_game(self)
        self.history = []
        self.moves = []
        self._uuid = self.board._uuid
        self.data = Namespace()
    
    def __repr__(self):
        return self.board._pprnt()
    
    def __hash__(self):
        return int(self._uuid) % (self.board.__hash__() + 1)
    
    def move(self, *args):
        self.history.append(self.board.fen_str())
        ret = self.board.move(*args)
        self.moves.append(self.board.lastmove)
        return ret
    
    def castle(self, *args):
        self.history.append(self.board.fen_str())
        self.board.castle(*args)
    
    def rollback(self):
        fen = self.history[-1]
        data = self.board.data
        cfg = self.data.cfg
        self.player1 = self.board.player1
        self.player2 = self.board.player2
        self.board = Board(self.player1, self.player2, fen)
        self.board.data = data
        self.board.cfg = cfg
    
    def ai_easy(self):
        from Phantom.ai.basic.mover import make_random_move
        try:
            return make_random_move(self.board)
        except:
            return self.ai_easy()  # keep trying until a move can be made
        
    def gui(self):
        from Phantom.constants import in_pythonista
        if in_pythonista:
            from Phantom.gui_pythonista.main_scene import MultiScene
            from Phantom.gui_pythonista.screen_main import ChessMainScreen
            from Phantom.gui_pythonista.screen_loading import ChessLoadingScreen
            self.data['screen_main'] = ChessMainScreen(self)
            self.data['screen_load'] = ChessLoadingScreen()
            self.data['main_scene'] = MultiScene(self.data['scene_load'])
            self.data['main_scene'].set_load_scene(self.data['scene_load'])
            self.data['main_scene'].set_main_scene(self.data['scene_main'])
            self.data['screen_main'].parent = self.data['main_scene']
            self.data['screen_load'].parent = self.data['main_scene']
            import scene
            scene.run(self.data['main_scene'])
__all__.append('ChessGame')

if __name__ == '__main__':
    g = ChessGame()
    g.board.cfg.disp_sqrs = False

