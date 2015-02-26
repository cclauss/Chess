# -*- coding: utf-8 -*-

"""Generate a tree for a given board."""

from Phantom.ai.tree.leaves import Node
from Phantom.ai.settings import window, maxdepth
from Phantom.core.board import Board
from Phantom.utils.debug import call_trace, log_msg
import sys

def _spawn_children(node):
    log_msg('_spawn_children({}) starting'.format(node), 4)
    legal = node.board.all_legal()
    for piece in legal:
        for move in legal[piece]:
            new = node.variate(piece.coord, move)
            newnode = Node(node.depth - 1, False, new)
            newnode.set_parent(node)
    log_msg('_spawn_children({}) ending'.format(node), 4)

def _recursive_spawn(node):
    log_msg('_recursive_spawn({}) starting'.format(node), 4)
    depth = node.depth
    if depth > maxdepth:
        return False
    for child in node.children:
        _spawn_children(child)
        _recursive_spawn(child)
    log_msg('_recursive_spawn({}) ending'.format(node), 4)

@call_trace(4)
def spawn_tree(board):
    root = Node(0, False, board)
    _spawn_children(root)
    _recursive_spawn(root)
    return root

