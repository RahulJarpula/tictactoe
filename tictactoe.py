"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #in the initial game state X gets the first move,
    #After X, y should be the one who is moving
    #A normal state; If in a row or column; sum(X)-sum(y)==0 then it is X's turn
    if sum(row.count("X") for row in board) - sum(row.count("O") for row in board) == 0:
        return 'X'
    else:
        return 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #Initially board is empty this returns the places where X and O can be put
    actions=set()
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j]== EMPTY:
                actions.add((i,j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #make a deep copy because you will need minimax algo to do the same on your board
    i, j = action
    # Check if action coordinates are valid
    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == EMPTY:
        # Make a deep copy to avoid modifying the original board
        new_board = deepcopy(board)
        new_board[i][j] = player(board) #updating actions into the set
        return new_board
    else:
        raise Exception("Invalid Action")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
   #idea is designating every X value from actions as 1 and O value as zero ; if sumX==3 then X
   #is winner elif sumO==0 then O is winner else game is drawn
    #checking rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'
    #checking columns
    for col in range(0, len(board[0])):
        if all(row[col] == 'X' for row in board):
            return 'X'
        elif all(row[col] == 'O' for row in board):
            return 'O'
    #checking diagonals
    if all(board[i][i] == 'X' for i in range(0,len(board))) or all(board[i][2 - i] == 'X' for i in range(0,len(board))):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(0,len(board))) or all(board[i][2 - i] == 'O' for i in range(0,len(board))):
        return 'O' 
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #declaring the state of the game is over either the game might be completed
    #both because of a draw or win
    #It should return true if game is over
    if winner(board) is not None:
        return True
    #checking if game is running 
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] is None:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)=='X':
        return 1
    elif winner(board)=='O':
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if terminal(board):
        return None
    if player(board) == 'X':
        return max(actions(board), key=lambda a: min_value(result(board, a)))
    else:
        return min(actions(board), key=lambda a: max_value(result(board, a)))
