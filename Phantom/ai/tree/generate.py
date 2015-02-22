# -*- coding: utf-8 -*-

"""Generate a tree for a given board."""

from Phantom.ai.tree.leaves import Node
from Phantom.ai.settings import window, maxdepth
import sys

def _spawn_subchildren(node):
    for child in node.children:
        child.spawn_children()
        _spawn_subchildren(child)

def make_tree(game):
    olim = sys.getrecursionlimit()
    sys.setrecursionlimit(2*olim)
    
    root = Node(0, False, game.board)
    root.spawn_children()
    _spawn_subchildren(root)
    
    sys.setrecursionlimit(olim)
    
    return root

