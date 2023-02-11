"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_c = 0
    o_c = 0
    for row in board:
        for i in row:
            if i == X:
                x_c += 1
            elif i == O:
                o_c += 1

    return X if x_c <= o_c else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    if len(set([board[i][i] for i in range(3)])) == 1:
        return board[1][1]
    elif len(set([board[i][2 - i] for i in range(3)])) == 1:
        return board[1][1]

    for i in range(3):
        if len(set([row[i] for row in board])) == 1:
            return board[i][i]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for _ in board:
        if EMPTY in _:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        return maxval(board)[1]
    elif player(board) == O:
        return minval(board)[1]


def maxval(board):
    if terminal(board):
        return utility(board), None
    t = v = -math.inf
    a = None
    for action in actions(board):
        v = max(v, minval(result(board, action))[0])
        if v > t:
            t = v
            a = action
    return v,a


def minval(board):
    if terminal(board):
        return utility(board), None
    t = v = math.inf
    a = None
    for action in actions(board):
        v = min(v, maxval(result(board, action))[0])
        if v < t:
            t = v
            a = action
    return v,a
