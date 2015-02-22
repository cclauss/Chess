# -*- coding: utf-8 -*-

"""The basics of the basics."""

from Phantom.ai.settings import scores, colors, king_material

def pos_eval_basic(board):
    score = 0
    for piece in board.pieces:
        piecescore = scores[piece.ptype] * colors[piece.color.color]
        score += piecescore
    return score

def pos_material(board):
    score = 0
    for piece in board.pieces:
        if piece.ptype == 'king':
            score += king_material
        else:
            score += scores[piece.ptype]
    return score

