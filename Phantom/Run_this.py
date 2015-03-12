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
from Phantom.core.coord.point import Coord

game = ChessGame()
print "PhantomChess Copyright (C) 2015 671620616"
print "This program comes with ABSOLUTELY NO WARRANTY; for details enter license"
print "This is free software, and you are welcome to redistribute it"
print "under certain conditions; type license for details."
print
print "Your game can be displayed by typing 'game'"
print "To move, type 'e2e4' or similar."
print "To execute a function, simply type the function as you normally would."
print "To exit, type 'quit' or close the program."
print "For a full list of commands, type 'help'."

print game

if __name__ == '__main__':
    import re
    help_str = """
    e2e4                  Move a piece from e2 to e4
    e2                    Get information about the piece at e2
    game                  Show the current layout of the game
    save xxxxxxx          Save the game under the name xxxxxxx
    load xxxxxxx          Load the game named xxxxxxx
    saves                 Get a list of all saved games
    gui                   Activate a GUI (Pythonista)
    quit                  Exit the game
    help                  Show this help text
    reset                 Reset the game to the opening position
    license               Show license information (it's a long read)
    
    ===== AI commands =====
        Prefix all commands listed below with "ai "
        Example: "ai rate"
        
        easy              Make a random move
        hard              Make a smart move
        rate              Get an integer representing the positional score of the board
    """
    move_re = re.compile(r'[a-h][1-8][a-h][1-8]')
    coord_re = re.compile(r'[a-h][1-8]')
    save_re = re.compile(r'save [a-zA-Z0-9\x20]+')
    load_re = re.compile(r'load [a-zA-Z0-9\x20]+')
    game_re = re.compile(r'game')
    quit_re = re.compile(r'quit')
    gui_re = re.compile(r'gui')
    help_re = re.compile(r'help')
    saves_re = re.compile(r'saves')
    rst_re = re.compile(r'reset')
    aieasy_re = re.compile(r'ai easy')
    aihard_re = re.compile(r'ai hard')
    airate_re = re.compile(r'ai rate')
    license_re = re.compile(r'license')
    def is_cmd(pattern, user):
        finds = pattern.findall(user)
        if finds == []: return False
        if finds[0] == user: return True
        return False
    running = True
    while running:
        user_in = raw_input(':> ')
        user_in = user_in.strip()
        try:
            if '(' in user_in or ')' in user_in:
                # assume a function was called
                exec user_in
            elif is_cmd(game_re, user_in):
                print game
            elif is_cmd(quit_re, user_in):
                running = False
                break
            elif is_cmd(save_re, user_in):
                game.board.save(' '.join(user_in.split()[1:]))
            elif is_cmd(load_re, user_in):
                from Phantom.core.game_class import loadgame
                game = loadgame(' '.join(user_in.split()[1:]))
            elif is_cmd(gui_re, user_in):
                game.gui()
            elif is_cmd(help_re, user_in):
                print help_str
            elif is_cmd(saves_re, user_in):
                from Phantom.boardio.load import listgames
                print listgames()
            elif is_cmd(rst_re, user_in):
                game = ChessGame()
                print game
            elif is_cmd(aieasy_re, user_in):
                game.ai_easy()
                print game
            elif is_cmd(aihard_re, user_in):
                game.ai_hard()
                print game
            elif is_cmd(airate_re, user_in):
                from Phantom.ai.pos_eval.advanced import pos_eval_advanced
                print pos_eval_advanced(game.board)
            elif is_cmd(license_re, user_in):
                print license()
            elif is_cmd(coord_re, user_in):
                print "\tGetting information for {}...".format(user_in)
                pos = Coord.from_chess(user_in)
                piece = game.board[pos]
                valid = [c.as_chess() for c in piece.valid()]
                promo = piece.is_promotable
                threatens = piece.threatens()
                threatened = piece.threatened_by()
                s = """    Piece at {}: {}
    Color: {}
    Valid moves: {}
    Is promotable: {}
    This piece threatens: {}
    This piece is threatened by: {}
    """.format(pos.as_chess(), piece, piece.color.color, valid, promo, threatens, threatened)
                print s
            else:
                # assume a move, like "e2e4"
                if is_cmd(move_re, user_in):
                    # is definitely a move
                    game.move(user_in)
                    print game
        except Exception as e:
            print "exception: {}".format(e)

