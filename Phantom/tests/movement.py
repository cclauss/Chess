# -*- coding: utf-8 -*-

"""Test the Phantom.core.board.Board.move() method"""

from Phantom.core.board import Board
from Phantom.utils.debug import log_msg, clear_log

def main():
    clear_log()
    b = Board()  # white to move, opening layout
    try:
        b.move('e2e4')
    except Exception as e:
        log_msg('Phantom.core.board.Board.move() method test failed:\n{}'.format(e), 0)
        import sys
        return sys.exc_info()

if __name__ == '__main__':
    exc = main()

