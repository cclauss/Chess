# -*- coding: utf-8 -*-

"""The code that makes the AI do stuff."""

from Phantom.core.board import Board
from Phantom.core.coord.point import Coord
from Phantom.core.exceptions import InvalidMove, InvalidDimension, ChessError, LogicError
import random

def make_random_move(board):
    moved = board
    board.freeze()
    piece = random.choice(board.pieces)
    board.unfreeze()
    if len(piece.valid) <= 0:
        return make_random_move(board)
    else:
        move = random.choice(piece.valid)
        board.move(piece.coord, move)
        moved = board
    return moved

