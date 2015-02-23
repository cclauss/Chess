# -*- coding: utf-8 -*-

"""Test the game class itself."""

from Phantom.core.game_class import ChessGame
from Phantom.utils.debug import log_msg

def main():
    g = None
    try:
        g = ChessGame()
    except Exception as e:
        log_msg('ChessGame instantiation test failed:\n{}'.format(e), 0)
    return g

if __name__ == '__main__':
    main()

