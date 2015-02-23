# -*- coding: utf-8 -*-

"""A search algorithim faster than minimax but guaranteed to give the same result."""


# Pseudocode
# src- Wikipedia article on alpha-beta pruning
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#01 function alphabeta(node, depth, α, β, maximizingPlayer)
#02      if depth = 0 or node is a terminal node
#03          return the heuristic value of node
#04      if maximizingPlayer
#05          v := -∞
#06          for each child of node
#07              v := max(v, alphabeta(child, depth - 1, α, β, FALSE))
#08              α := max(α, v)
#09              if β ≤ α
#10                  break (* β cut-off *)
#11          return v
#12      else
#13          v := ∞
#14          for each child of node
#15              v := min(v, alphabeta(child, depth - 1, α, β, TRUE))
#16              β := min(β, v)
#17              if β ≤ α
#18                  break (* α cut-off *)
#19          return v
#(* Initial call *)
#alphabeta(origin, depth, -∞, +∞, TRUE)

def alpha_beta_value(node, depth, alpha, beta, maximizing):
    if depth == 0 or node.is_terminal:
        return node.score
    if maximizing:
        v = float('-inf')
        for child in node.children:
            v = max(v, alpha_beta_value(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
    else:
        v = float('inf')
        for child in node.children:
            v = min(v, alpha_beta_valie(child, depth - 1, alpha, beta, True))
            beta = min(beta, v)
            if b <= alpha:
                break
    return v


# Initial call would be 
# `alpha_beta_value(root, Chess.ai.settings.maxdepth, float('-inf'), float('inf'), True)`

