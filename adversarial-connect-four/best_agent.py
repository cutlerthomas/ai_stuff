import connect_four_model as model
from pettingzoo.classic import connect_four_v3
import copy
import math
import numpy as np


class Node:

    def __init__(self, parent, action, max, score, children, original):
        self.parent = parent
        self.action = action
        self.max = max
        self.score = score
        self.children = children
        self.original = original


def check_for_three(env):
    board = np.array(env.board).reshape(6, 7)
    piece = env.current_agent + 1
    three_count = 0
    # Check horizontal locations for win
    column_count = 7
    row_count = 6
    for c in range(column_count - 3):
        for r in range(row_count):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == 0
            ):
                three_count += 1

        # Check vertical locations for win
    for c in range(column_count):
        for r in range(row_count - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == 0
            ):
                three_count += 1

    # Check positively sloped diagonals
    for c in range(column_count - 3):
        for r in range(row_count - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == 0
            ):
                three_count += 1

    # Check negatively sloped diagonals
    for c in range(column_count - 3):
        for r in range(3, row_count):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == 0
            ):
                three_count += 1

    return three_count

def check_for_two(env):
    board = np.array(env.board).reshape(6, 7)
    piece = env.current_agent + 1
    two_count = 0
    # Check horizontal locations for win
    column_count = 7
    row_count = 6
    for c in range(column_count - 3):
        for r in range(row_count):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == 0
                and board[r][c + 3] == 0
            ):
                two_count += 1

    # Check vertical locations for win
    for c in range(column_count):
        for r in range(row_count - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == 0
                and board[r + 3][c] == 0
            ):
                two_count += 1

    # Check positively sloped diagonals
    for c in range(column_count - 3):
        for r in range(row_count - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == 0
                and board[r + 3][c + 3] == 0
            ):
                two_count += 1

    # Check negatively sloped diagonals
    for c in range(column_count - 3):
        for r in range(3, row_count):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == 0
                and board[r - 3][c + 3] == 0
            ):
                two_count += 1

    return two_count

def MiniMax(env, depth, max):
    if depth == 0 or env.game_over():
        if max == True:
            return EVALUATE(env, "maxi")
        else:
            return EVALUATE(env, "mini")
    if max == True:
        max_score = -math.inf
        for move in env.legal_moves():
            env1 = copy.deepcopy(env)
            env1.step(move)
            score = MiniMax(env1, depth - 1, False)
            if score > max_score:
                max_score = score
        return max_score
    else:
        min_score = math.inf
        for move in env.legal_moves():
            env1 = copy.deepcopy(env)
            env1.step(move)
            score = MiniMax(env1, depth - 1, True)
            if score < min_score:
                min_score = score
        return min_score
    
def find_best_move(env, depth):
    best_move = None
    best_score = -math.inf
    for move in env.legal_moves():
        env1 = copy.deepcopy(env)
        env1.step(move)
        score = MiniMax(env1, depth, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def EVALUATE(env, agent):
    searchable_env = copy.deepcopy(env)
    score = 0
    if agent == "mini":
        if env.game_over():
            score = 100
        elif check_for_three(env) == 1:
            score += 10
        elif check_for_three(env) >= 2:
            score += 25
        else:
            if check_for_two(env) >= 1:
                score += 1
    elif agent == "maxi":
        if env.game_over():
            score = -100
        elif check_for_three(env) == 1:
            score -= 10
        elif check_for_three(env) >= 2:
            score -= 25
        else:
            if check_for_two(env) >= 1:
                score -= 1
    else:
        print("invalid agent given")
    return score

def agent_function(env, agent):
    observation, reward, termination, truncation, info = env.last()
    if termination or truncation:
        action = None
    else:
        action = None
        searchable_env = model.ConnectFour()
        searchable_env.copy_from_env(env)
        action = find_best_move(searchable_env, 5)
        
    return action