# -*- coding: utf-8 -*-

"""Test the advanced position evaluator."""

from Phantom.core.game_class import ChessGame
from Phantom.ai.pos_eval.advanced import pos_eval_advanced
from Phantom.utils.debug import log_msg

def main():
    game = ChessGame('Game 1')
    score = None
    try:
        score = pos_eval_advanced(game.board)
    except Exception as e:
        log_msg('Advanced position evaluation failed: \n{}'.format(e), 0)
    return score

if __name__ == '__main__':
    r = main()

