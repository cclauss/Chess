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

"""To start a new game, simply run this file."""

from Phantom.core.game_class import ChessGame
from Phantom.docs.documentation import program_use
from Phantom.utils.lic import license

game = ChessGame()
print "PhantomChess Copyright (C) 2015 671620616"
print "This program comes with ABSOLUTELY NO WARRANTY; for details enter license()"
print "This is free software, and you are welcome to redistribute it"
print "under certain conditions; type license() for details."

print "Your game can be accessed through the variable 'game'."
print "To make a move, type `game.move('e2e4')` or similar."
print "For additional help, type `print program_use()`"

print game

if __name__ == '__main__':
    while True:
        input = raw_input('>>> ')
        if input == 'game':
            print game
        else:
            exec input

