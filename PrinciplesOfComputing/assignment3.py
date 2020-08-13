"""
Monte Carlo Tic-Tac-Toe Player
"""

import random

try:
    import simplegui
    import codeskulptor
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor

import lib.poc_ttt_gui as gui
import lib.poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player


# Add your functions here.
def mc_trial(board, player):
    '''
    :param board: current game board
    :param player: current player
    :return: None
    '''
    empty_squares = board.get_empty_squares()
    while empty_squares:
        square = random.choice(empty_squares)
        board.move(square[0], square[1], player)
        empty_squares.remove(square)
        if board.check_win():
            break
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    '''
    :param scores: current game scores
    :param board: current game board
    :param player: current player
    :return: None
    '''
    winner = board.check_win()
    size = board.get_dim()
    for row in range(size):
        for col in range(size):
            square = board.square(row, col)
            if square == provided.PLAYERX:
                if winner == provided.PLAYERX:
                    scores[row][col] += SCORE_CURRENT
                elif winner == provided.PLAYERO:
                    scores[row][col] += -SCORE_OTHER
            elif square == provided.PLAYERO:
                if winner == provided.PLAYERX:
                    scores[row][col] += -SCORE_CURRENT
                elif winner == provided.PLAYERO:
                    scores[row][col] += SCORE_OTHER


def get_best_move(board, scores):
    '''
    :param board: current game board
    :param scores: current game scores
    :return: move in the form of (row, column)
    '''
    empty_squares = board.get_empty_squares()
    max_score = max([scores[r][c] for r, c in empty_squares])
    moves = [(r, c) for r, c in empty_squares if scores[r][c] == max_score]
    return random.choice(moves)


def mc_move(board, player, trials):
    '''
    :param board: current game board
    :param player: current player
    :param trials: number of game trials
    :return: move in the form of (row, column)
    '''
    size = board.get_dim()
    scores = [[0 for _ in range(size)] for _ in range(size)]
    for _ in range(trials):
        cloned = board.clone()
        mc_trial(cloned, player)
        mc_update_scores(scores, cloned, player)
    return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
