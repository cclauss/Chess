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
print
print "Your game can be displayed by typing 'game'"
print "To move, type 'e2e4' or similar."
print "To execute a function, simply type the function as you normally would."
print "To exit, type 'quit' or close the program."

print game

if __name__ == '__main__':
    import re
    move_re = re.compile(r'[a-h][1-8][a-h][1-8]')
    save_re = re.compile(r'save [a-zA-Z0-9\x20]+')
    load_re = re.compile(r'load [a-zA-Z0-9\x20]+')
    is_move = lambda s: move_re.findall(s) if move_re.findall(s) != [] else [0]
    is_save = lambda s: save_re.findall(s) if save_re.findall(s) != [] else [0]
    is_load = lambda s: load_re.findall(s) if load_re.findall(s) != [] else [0]
    running = True
    while running:
        user_in = raw_input(':> ')
        try:
            if '(' in user_in or ')' in user_in:
                # assume a function was called
                exec user_in
            elif user_in == 'game':
                print game
            elif user_in == 'quit':
                running = False
                break
            elif is_save(user_in)[0] == user_in:
                game.board.save(' '.join(user_in.split()[1:]))
            elif is_load(user_in)[0] == user_in:
                print user_in
                from Phantom.core.game_class import loadgame
                game = loadgame(' '.join(user_in.split()[1:]))
                print ' '.join(user_in.split()[1:])
            else:
                # assume a move, like "e2e4"
                if is_move(user_in)[0] == user_in:
                    # is definitely a move
                    game.move(user_in)
                    print game
        except Exception as e:
            print "exception: {}".format(e)

