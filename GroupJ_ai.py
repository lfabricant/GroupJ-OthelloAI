#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: YOUR NAME AND UNI 
"""

import random
import sys
import time
import math
count = 0
sys.setrecursionlimit(15)
#limit = sys.getrecursionlimit()

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

from othello_game import AiPlayerInterface

def compute_utility(board, color):
  score = get_score(board) # white, black
  if color == score[0]: # WHITE 
    return score[0]-score[1]
  else: #color == score[1] BLACK
    return score[1]-score[0]


############ MINIMAX ###############################

def minimax_min_node(board, color, count_depth):
  if color == 1:
    opponent_color = 2
  else:
    opponent_color = 1
  if count_depth == 0 or not get_possible_moves(board, color): 
    return compute_utility(board, color)
  else: 
    moves = get_possible_moves(board, opponent_color)
      #small = moves[0]
    utility = math.inf #compute_utility(small, color)
    for i in moves: # access each tuple pair of a move that could be played from this spot
      ##return max(all minimax min nodes in moves)
      b = play_move(board, opponent_color, i[0], i[1]) # new board orientation if the opponent moves here
      u = minimax_max_node(b, color, count_depth-1) # score for opponent if it moves here
      #count+=1
      if u < utility:
        utility = u  
      #if count > 5:
        #return utility      
    return utility 


def minimax_max_node(board, color, count_depth):
  if count_depth == 0 or not get_possible_moves(board,color):
    return compute_utility(board, color)
  else:
    moves = get_possible_moves(board, color)
      #large = moves[0]
    utility = -math.inf #compute_utility(large, color)
    for i in moves: # access each tuple pair of a move that could be played from this spot
      ##return max(all minimax min nodes in moves)
      b = play_move(board, color, i[0], i[1]) # new board orientation if the opponent moves here
      u = minimax_min_node(b, color, count_depth-1) # score for opponent if it moves here
     # count+=1
      if u > utility:
        utility = u
      #if(sys.getrecursionlimit()):
       # return utility
      #if count > 5:
      #  return utility
    return utility

def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    count_depth = 15
    start = 
    li = get_possible_moves(board, color)
    best_move = None
    highest_score = -math.inf
    #while not limit:
    for i in li: 
      
      score = minimax_min_node(board, color, count_depth)
      #count+=1
      if score > highest_score: 
        highest_score = score
        best_move = i
       # count+=1
      if sys.getrecursionlimit() or :
        return best_move
    return best_move

#def depth_limit()
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
  if not get_possible_moves(board,color):
    return compute_utility(board, color)
  v = math.inf
  for a in get_possible_moves(board, color): #color
    v = min(v, alphabeta_max_node(play_move(board, color, a[0], a[1]), color, alpha, beta))
    if v <= alpha:
      return v
    beta = min(beta, v)
  return v

#alphabeta_max_node(board, color, alpha, beta, level, limit)

def alphabeta_max_node(board, color, alpha, beta):
  if not get_possible_moves(board,color):
    return compute_utility(board, color)
  v = -math.inf
  for a in get_possible_moves(board, color): #color
    v = max(v, alphabeta_min_node(play_move(board, color, a[0], a[1]), color, alpha, beta))
    if v >= beta:
      return v
    alpha = max(alpha, v)
  return v


def select_move_alphabeta(board, color): 
  v = alphabeta_max_node(board, color, -math.inf, math.inf)
  for a in get_possible_moves(board, color):
    if a == v:
      return a
  return None
 ## PSEUDOCODE - (https://www.endtoend.ai/mooc/aind/12/)

  #best_move = None
  #highest_score = -math.inf
  #li = get_possible_moves(board, color)
  #for i in li: 
  #  score = alphabeta_max_node(board, color, -math.inf, math.inf)
      #count+=1
    #if score > highest_score: 
      #highest_score = score
      #best_move = i
       # count+=1
     # if count > 5:
       # return best_move
  #return best_move


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)              
            # Select the move and send it to the manager 
            #movei, movej = select_move_minimax(board, color)
            movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
  run_ai()

