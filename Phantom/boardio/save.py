# -*- coding: utf-8 -*-

"""Save a game."""

import os
import inspect

# implementation detail 4

format = '{name}: {fen}\n'
savefilename = 'savegames.txt'

def save(board):
    
    origdir = os.getcwd()
    savedir = os.path.split(inspect.getfile(save))[0]
    os.chdir(savedir)

    newline = format.format(name=board.name, fen=board.fen_str())
    
    with open(savefilename, 'a') as f:
        f.write(newline)
    
    os.chdir(origdir)

