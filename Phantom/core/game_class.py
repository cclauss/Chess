# -*- coding: utf-8 -*-

"""The class that holds a complete game of Chess.

Generally, use this class rather than Phantom.core.board.Board, because this class
keeps track of history, which Board doesn't."""

from Phantom.core.board import Board, Tile, load as _loadboard
from Phantom.core.players import Player, Side
from Phantom.core.pieces import ChessPiece, Pawn, Rook, Knight, Bishop, King, Queen
from Phantom.core.exceptions import ChessError, LogicError, InvalidMove, InvalidDimension
from Phantom.core.coord import *
from Phantom.boardio.boardcfg import Cfg
from Phantom.boardio.load import listgames

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
    
    def __repr__(self):
        return self.board._pprnt()
    
    def __hash__(self):
        return int(self._uuid) % (self.board.__hash__() + 1)
    
    def move(self, *args):
        self.history.append(self.board.fen_str())
        self.board.move(*args)
        self.moves.append(self.board.lastmove)
    
    def castle(self, *args):
        self.history.append(self.board.fen_str())
        self.board.castle(*args)
    
    def rollback(self):
        fen = self.history[-1]
        self.player1 = self.board.player1
        self.player2 = self.board.player2
        self.board = Board(self.player1, self.player2, fen)
    
    def ai_easy(self):
        from Phantom.ai.basic.mover import make_random_move
        try:
            return make_random_move(self.board)
        except:
            return self.ai_easy()  # keep trying until a move can be made

if __name__ == '__main__':
    games = listgames()
    g = ChessGame('kaufman 2')
    g.board.cfg.disp_sqrs = False

