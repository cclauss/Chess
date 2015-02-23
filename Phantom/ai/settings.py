# -*- coding: utf-8 -*-

"""A separate constants.py file to save some space in the main one."""

maxdepth = 2
window = 20

# Points-per-piece simple
scores = dict(
pawn = 100.0
,knight = 300.0
,bishop = 300.0
,rook = 500.0
,queen = 900.0
,king = 1e10)

king_material = 400  # use the endgame score for material worth totalling

colors = dict(
white = 1
,black = -1)

# Advanced heuristic scores
knight_on_edge_score = 150.0
developed_scores = dict(
pawn = 70.0
,knight = 350.0
,bishop = 400.0
,rook = 600.0
,queen = 1000.0
,king = 0)  # king development will be tested in a different heuristic
advanced_pawn_mul = 40.0
king_endgame = 400.0
bishop_pair_bonus = 50.0
castle_opening_bonus = 250.0
castle_midgame_bonus = 100.0
castle_endgame_bonus = -400.0
doubled_pawn = -50.0
tripled_pawn = -75.0
pawn_ram = -75.0
isolated_pawn = -100.0
eight_pawns = -75
passed_pawn = 250.0
mobility_mul = 10.0  # although move moves are better, most possible moves in chess are pointless
bishop_open_bonus = -170.0
knight_closed_bonus = 40.0

