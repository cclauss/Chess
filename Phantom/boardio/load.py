# -*- coding: utf-8 -*-

"""Get a FEN string for a given board save-name."""

from Phantom.core.exceptions import ChessError, LogicError
from Phantom.constants import save_fen
import os
import inspect

def loadgame(name):
    
    orig_dir = os.getcwd()
    save_dir = os.path.split(inspect.getfile(loadgame))[0]
    os.chdir(save_dir)
    
    with open(save_fen, 'r') as file_read:
        lines = file_read.readlines()
    
    os.chdir(orig_dir)
    
    for line in lines:
        line = line.strip()
        if (line == '') or (line[0] == '#'):
            continue
        split = line.index(':')
        bname = line[:split]
        fen = line[split+1:]
        if bname == name:
            return fen

def listgames():
    
    orig_dir = os.getcwd()
    save_dir = os.path.split(inspect.getfile(listgames))[0]
    os.chdir(save_dir)
    
    with open(save_fen, 'r') as file_read:
        lines = file_read.readlines()
    
    os.chdir(orig_dir)
    
    ret = []
    for line in lines:
        line = line.strip()
        if (line == '') or (line[0] == '#'):
            continue
        split = line.index(':')
        name = line[:split]
        ret.append(name)
    
    return ret

