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

"""Save a game."""

from Phantom.constants import save_fen
import os
import inspect

# implementation detail 4

format = '{name}: {fen}\n'

def save(board):
    
    origdir = os.getcwd()
    savedir = os.path.split(inspect.getfile(save))[0]

    newline = '{}: {}\n'.format(board.name, board.fen_str())
    
    with open(os.path.join(savedir, save_fen), 'a') as f:
        f.write(newline)

