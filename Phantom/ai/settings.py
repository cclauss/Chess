# -*- coding: utf-8 -*-

#########################################################################
# This file is part of PhantomChess.                                    #
#                                                                       #
# PhantomChess is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  # 
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# PhantomChess is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        # 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with PhantomChess.  If not, see <http://www.gnu.org/licenses/>. #
#########################################################################

"""A separate constants.py file to save some space in the main one."""

maxdepth = 2
window = 20

# Points-per-piece simple
scores = dict(
pawn = 100.0
,knight = 320.0
,bishop = 330.0
,rook = 500.0
,queen = 900.0
,king = 20000)  # use 20000 to signal the capture of a king is better than all other options

king_material = 400  # use the endgame score for material worth totalling

colors = dict(
white = 1
,black = -1)

# Advanced heuristic scores

# avoid a knight on the edge; they are bad
knight_on_edge_score = -50.0

# use a different set of scores for farther developed pieces
developed_scores = dict(
pawn = 70.0
,knight = 350.0
,bishop = 400.0
,rook = 600.0
,queen = 1000.0
,king = 0)  # king development will be tested in a different heuristic

# pawns closer to promotion are much better
advanced_pawn_mul = 40.0

# the king gets a score in the endgame but not opening/midage
king_endgame = 400.0

# bonus for having both bishops
bishop_pair_bonus = 50.0

# castling is good in the opening, ok in the midgame, but pointless in the endgame
castle_opening_bonus = 250.0
castle_midgame_bonus = 100.0
castle_endgame_bonus = -400.0

# pawn structure analysis
doubled_pawn = -50.0
tripled_pawn = -75.0
pawn_ram = -75.0
isolated_pawn = -40.0
eight_pawns = -75
passed_pawn = 250.0

# although move moves are better, most possible moves in chess are pointless
mobility_mul = 10.0

# bishops where there are many pawns on the same color squares as the bishops
# are less useful
bad_bishop_mul = 30.0

