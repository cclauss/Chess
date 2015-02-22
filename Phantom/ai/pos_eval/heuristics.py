# -*- coding: utf-8 -*-

"""A lot of rules that analyze a board.

All functions in this file take one argument, a board, and analyze it
for a specific characteristic. 
They all return a number which should be added to the board variation's score.

The file defines an all_rules list that contains all the functions.  It can be iterated through
with a loop similar to the following to obtain a score for a board:

```
from Phantom.ai.pos_eval.heuristics import all_rules
from Phantom.ai.pos_eval.basic import pos_eval_basic
from Phantom.core.board import Board

test = Board()
score = pos_eval_basic(test)  # should be 0
print "Basic evaluation:", score

for rule in all_rules:
    score += rule(test)
    print "Applied {} rule, score:".format(rule.__name__), score

print "Final score:", score
```
""" 

from Phantom.ai.phases import Phase
from Phantom.core.coord.point import Coord
from Phantom.constants import *

board_north_edge = [Coord(x, 7) for x in range(grid_width)]
board_south_edge = [Coord(x, 0) for x in range(grid_width)]
board_east_edge = [Coord(7, y) for y in range(grid_height)]
board_west_edge = [Coord(0, y) for y in range(grid_height)]
board_rim = board_north_edge + board_south_edge + board_east_edge + board_west_edge

a_file = [Coord(0, y) for y in range(grid_height)]
b_file = [Coord(1, y) for y in range(grid_height)]
c_file = [Coord(2, y) for y in range(grid_height)]
d_file = [Coord(3, y) for y in range(grid_height)]
e_file = [Coord(4, y) for y in range(grid_height)]
f_file = [Coord(5, y) for y in range(grid_height)]
g_file = [Coord(6, y) for y in range(grid_height)]
h_file = [Coord(7, y) for y in range(grid_height)]

all_rules = []

def knight_on_edge(board):
    from Phantom.ai.settings import knight_on_edge_score
    score = 0
    for piece in board.pieces:
        if piece.ptype == 'knight':
            if piece.coord in board_east_edge + board_west_edge:
                if piece.color == 'white':
                    score -= knight_on_edge_score
                else:
                    score += knight_on_edge_score
    return score
all_rules.append(knight_on_edge)

def developed_pieces(board):
    from Phantom.ai.settings import developed_scores
    score = 0
    for piece in board.pieces:
        if not piece.firstmove:
            if piece.color == 'white':
                score += developed_scores[piece.ptype]
            else:
                score -= developed_scores[piece.ptype]
    return score
all_rules.append(developed_pieces)

def advanced_pawns(board):
    from Phantom.ai.settings import advanced_pawn_mul
    from Phantom.constants import grid_height
    score = 0
    for piece in board.pieces:
        if piece.ptype == 'pawn':
            if piece.color == 'white':
                if piece.coord.y >= 4:
                    score += p.coord.y * advanced_pawn_mul
            elif piece.color == 'black':
                if piece.coord.y <= 3:
                    score -= (grid_height - p.coord.y) * advanced_pawn_mul
    return score
all_rules.append(advanced_pawns)

def rate_kings(board):
    from Phantom.ai.settings import king_endgame
    from Phantom.ai.phases import Phase
    score = 0
    if Phase.analyze(board) == Phase.endgame:
        for piece in board.pieces:
            if piece.ptype == 'king':
                if piece.color == 'white':
                    score += king_endgame
                elif piece.color == 'black':
                    score -= king_endgame
    return score
all_rules.append(rate_kings)

def bishop_pair(board):
    from Phantom.ai.settings import bishop_pair_bonus
    score = 0
    num_white_bishops = num_black_bishops = 0
    for piece in board.pieces:
        if piece.ptype == 'bishop':
            if piece.color == 'white':
                num_white_bishops += 1
            elif piece.color == 'black':
                num_black_bishops += 1
    if num_white_bishops >= 2:
        score += bishop_pair_bonus
    if num_black_bishops >= 2:
        score -= bishop_pair_bonus
    return score
all_rules.append(bishop_pair)

def has_castled(board):
    from Phantom.ai.settings import castle_opening_bonus, castle_midgame_bonus, castle_endgame_bonus
    from Phantom.ai.phases import Phase
    def sides_castled():
        ret = ['white', 'black']
        castle = board.castling_rights
        if ('K' in castle) or ('Q' in castle):
            ret.remove('white')
        if ('k' in castle) or ('q' in castle):
            ret.remove('black')
        return ret
    score = 0
    castled = sides_castled()
    phase = Phase.analyze(board)
    if phase == Phase.opening:
        if 'white' in castled:
            score += castle_opening_bonus
        if 'black' in castled:
            score -= castle_opening_bonus
    elif phase == Phase.midgame:
        if 'white' in castled:
            score += castle_midgame_bonus
        if 'black' in castled:
            score -= castle_midgame_bonus
    elif phase == Phase.endgame:
        if 'white' in castled:
            score += castle_endgame_bonus
        if 'black' in castled:
            score -= castle_endgame_bonus
    return score
all_rules.append(has_castled)

def pawn_structure(board):
    score = 0
    from Phantom.ai.settings import (doubled_pawn, tripled_pawn, isolated_pawn,
                                   pawn_ram, eight_pawns, passed_pawn)
    white_pawns = black_pawns = []
    for piece in board.pieces:
        if piece.ptype == 'pawn':
            if piece.color == 'white':
                white_pawns.append(piece)
            elif piece.color == 'black':
                black_pawns.append(piece)
    pawns = white_pawns + black_pawns
    
    if len(white_pawns) == 8:
        score += eight_pawns
    if len(black_pawns) == 8:
        score -= eight_pawns
    
    for pawn in white_pawns:
        if pawn.coord.y >= 5:
            score += passed_pawn
    for pawn in black_pawns:
        if pawn.coord.y <= 2:
            score -= passed_pawn
    
    

