# -*- coding: utf-8 -*-

"""Test the AI's basic position evaluation and material assesment."""

from Phantom.core.game_class import ChessGame
from Phantom.ai.pos_eval.basic import pos_eval_basic, pos_material
from Phantom.utils.debug import log_msg, clear_log

def main(clear=True):
    if clear: clear_log()
    log_msg('Testing Phantom.ai.pos_eval.basic pos_eval_basic() & pos_material()', 0)
    game = ChessGame()
    score = material = None
    try:
        score = pos_eval_basic(game.board)
    except Exception as e:
        log_msg('AI basic position evaluation failed: \n{}'.format(e), 0)
    try:
        material = pos_material(game.board)
    except Exception as e:
        log_msg('AI material assesment failed: \n{}'.format(e), 0)
    log_msg('Test complete', 0)
    return score, material

if __name__ == '__main__':
    main()

