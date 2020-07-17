"""
COMS W4701 Artificial Intelligence - Programming Homework 2

This module contains functions that are accessed by the game manager
and by the each AI player. Feel free to call these functions when 
building your AIs. 

@author: Daniel Bauer 
"""

def find_lines(board, i, j, player):
    """
    Find all the uninterrupted lines of stones that would be captured if player
    plays column i and row j. 
    """
    lines = []
    for xdir, ydir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], 
                       [-1, 0], [-1, 1]]:
        u = i
        v = j
        line = []

        u += xdir
        v += ydir
        found = False
        while u >= 0 and u < len(board) and v >= 0 and v < len(board):
            if board[v][u] == 0:
                break
            elif board[v][u] == player:
                found = True
                break
            else: 
               line.append((u,v))
            u += xdir
            v += ydir
        if found and line: 
            lines.append(line)
    return lines
   

def get_possible_moves(board, player):
    """
    Return a list of all possible (column,row) tuples that player can play on
    the current board. 
    """
    result = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] == 0:
                lines = find_lines(board,i,j,player)
                if lines: 
                    result.append((i,j))
    return result


def play_move(board, player, i, j):
    new_board = []
    for row in board: 
        new_board.append(list(row[:]))
    lines = find_lines(board, i,j, player)
    new_board[j][i] = player
    for line in lines: 
        for u,v in line: 
           new_board[v][u] = player 
    final = []
    for row in new_board: 
        final.append(tuple(row))
    return tuple(final) 

def get_score(board):
    p1_count = 0
    p2_count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1: 
              if (i == 0 and j == 0) or (i == len(board)-1 and j == 0) or (i == len(board)-1 and j == len(board)-1) or (i == 0 and j == len(board)-1):
                p1_count += 2
              else:  
                p1_count += 1
            elif board[i][j] == 2:
              if (i == 0 and j == 0) or (i == len(board)-1 and j == 0) or (i == len(board)-1 and j == len(board)-1) or (i == 0 and j == len(board)-1):
                p2_count += 2
              else:
                p2_count += 1
    return p1_count, p2_count



