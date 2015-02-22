# -*- coding: utf-8 -*-

"""A minimax algorithim

By chance, this happens to be a clean import.  Nothing is needed.
"""

# Pseudocode
# src- Wikipedia article on minimax algorithim
#––––––––––––––––––––––––––––––––––––––––––––––––––––
# function minimax(node, depth, maximizingPlayer)
#     if depth = 0 or node is a terminal node
#         return the heuristic value of node
#     if maximizingPlayer
#         bestValue := -∞
#         for each child of node
#             val := minimax(child, depth - 1, FALSE)
#             bestValue := max(bestValue, val)
#         return bestValue
#     else
#         bestValue := +∞
#         for each child of node
#             val := minimax(child, depth - 1, TRUE)
#             bestValue := min(bestValue, val)
#         return bestValue
# 
# (* Initial call for maximizing player *)
# minimax(origin, depth, TRUE)

def minimax_value(node, depth, maximizing):
    if depth == 0 or node.is_terminal:
        return node.score
    if maximizing:
        f = max
        bestvalue = float('-inf')
    else:
        f = min
        bestvalue = float('inf')
    for child in node.children:
        val = minimax_value(child, depth - 1, not maximizing)
        bestvalue = f(bestvalue, val)
    return bestvalue

