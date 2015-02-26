# -*- coding: utf-8 -*-

"""Test the advanced position evaluator."""

from Phantom.core.game_class import ChessGame
from Phantom.ai.pos_eval.advanced import pos_eval_advanced
from Phantom.utils.debug import log_msg, clear_log

def main(clear=True):
    if clear: clear_log()
    log_msg('Testing Phantom.ai.pos_eval.advanced.pos_eval_advanced()', 0)
    game = ChessGame('Game 1')
    score = None
    try:
        score = pos_eval_advanced(game.board)
    except Exception as e:
        log_msg('Advanced position evaluation failed: \n{}'.format(e), 0, err=True)
    finally:
        log_msg('Test complete', 0)
    return score

if __name__ == '__main__':
    r = main()

