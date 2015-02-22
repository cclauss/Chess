# -*- coding: utf-8 -*-

"""An interface to the heuristics file."""

def pos_eval_advanced(board):
    from Phantom.ai.pos_eval.heuristics import all_rules
    from Phantom.ai.pos_eval.basic import pos_eval_basic
    
    score = pos_eval_basic(board)
    
    for rule in all_rules:
        score += rule(board)
    
    return score

