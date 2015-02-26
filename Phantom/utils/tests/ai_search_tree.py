# -*- coding: utf-8 -*-

"""Test the AI's search tree generation."""

from Phantom.ai.tree.leaves import Node
from Phantom.ai.tree.generate import spawn_tree
from Phantom.core.game_class import ChessGame
from Phantom.utils.debug import log_msg, clear_log

def main(clear=True):
    if clear: clear_log()
    log_msg('Testing Phantom.ai.tree.generate.spawn_tree()', 0)
    tree = None
    try:
        g = ChessGame()
        tree = spawn_tree(g.board)
    except Exception as e:
        log_msg('Phanotm.ai.tree.generate.spawn_tree() test failed:\n{}'.format(e), 0, err=True)
    finally:
        log_msg('Test complete', 0)
    return tree

if __name__ == '__main__':
    tree = main()

