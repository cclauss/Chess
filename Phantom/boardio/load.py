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

"""Get a FEN string for a given board save-name."""

from Phantom.core.exceptions import ChessError, LogicError
from Phantom.constants import save_fen, phantom_dir
import os
#import inspect

def loadgame(name):
    
    read = os.path.join(phantom_dir, 'boardio', save_fen)
    with open(read, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        bname, _, fen = line.partition(':')
        if bname == name:
            return fen

def listgames():
    
    read = os.path.join(phantom_dir, 'boardio', save_fen)
    with open(read, 'r') as f:
        lines = f.readlines()
    
    ret = []
    for line in lines:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        name = line.partition(':')[0]
        ret.append(name)
    
    return ret
