# -*- coding: utf-8 -*-

"""Welcome to Phantom! For help, see Phantom/docs/.

The module IS import * safe, however, it is generally cleaner to use a direct import.
"""

from Phantom.core.board import Tile, Board
from Phantom.core.pieces import ChessPiece, Pawn, Knight, Bishop, Rook, Queen, King
from Phantom.core.players import Side, Player
from Phantom.core.exceptions import ChessError, LogicError, InvalidMove, InvalidDimension
from Phantom.core.game_class import ChessGame
from Phantom.core.coord.point import Coord, Grid
from Phantom.core.coord.vectored_lists import north, south, east, west, ne, se, nw, sw
from Phantom.core.coord.dirs import dirfinder
import Phantom.core.coord as coord
import Phantom.core as core

from Phantom.boardio.save import save
from Phantom.boardio.load import loadgame, listgames
from Phantom.boardio.boardcfg import Cfg
import Phantom.boardio as boardio

