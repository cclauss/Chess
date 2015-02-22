# -*- coding: utf-8 -*-

"""Get a FEN string for a given board save-name."""

from Phantom.core.exceptions import ChessError, LogicError
import os
import inspect

savefilename = 'savegames.txt'

def loadgame(name):
    
    orig_dir = os.getcwd()
    save_dir = os.path.split(inspect.getfile(loadgame))[0]
    os.chdir(save_dir)
    
    with open(savefilename, 'r') as file_read:
        lines = file_read.readlines()
    
    os.chdir(orig_dir)
    
    for line in lines:
        split = line.index(':')
        bname = line[:split]
        fen = line[split+1:]
        if bname == name:
            return fen

def listgames():
    
    orig_dir = os.getcwd()
    save_dir = os.path.split(inspect.getfile(listgames))[0]
    os.chdir(save_dir)
    
    with open(savefilename, 'r') as file_read:
        lines = file_read.readlines()
    
    os.chdir(orig_dir)
    
    ret = []
    for line in lines:
        split = line.index(':')
        name = line[:split]
        ret.append(name)
    
    return ret

