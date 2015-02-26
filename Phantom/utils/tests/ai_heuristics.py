# -*- coding: utf-8 -*-

"""Test the AI's position evaluation heuristics, one at a time and print the output."""

from Phantom.utils.debug import log_msg, clear_log
from Phantom.ai.pos_eval.heuristics import all_rules
from Phantom.core.game_class import ChessGame

def main(clear=True):
    if clear: clear_log()
    log_msg('Testing Phantom.ai.pos_eval.heuristics functions', 0)
    g = ChessGame('Game 1')
    log_msg('Testing AI heuristics on savegame "Game 1":', 0)
    score = 0
    for rule in all_rules:
        try:
            log_msg(rule.__name__ + " evaluating...", 0)
            r = rule(g.board)
            log_msg(rule.__name__ + ' returned {}'.format(r), 0)
            score += r
        except Exception as e:
            log_msg('{} failed:\n{}'.format(f.__name__, e), 0, err=True)
    log_msg('Test complete', 0)
    
    return score

if __name__ == '__main__':
    score = main()

