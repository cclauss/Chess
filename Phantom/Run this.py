# -*- coding: utf-8 -*-

"""To start a new game, simply run this file."""

from Phantom.core.game_class import ChessGame
from Phantom.core.board import load
from Phantom.boardio.load import listgames
from Phantom.docs.documentation import program_use

game = ChessGame()
print "Your game can be accessed through the variable 'game'."
print "To make a move, type `game.move('e2e4')` or similar."
print "For additional help, type `print program_use()`"
print game

