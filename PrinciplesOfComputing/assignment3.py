"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player


# Add your functions here.
def mc_trial(board, player):
    while not board.check_win():
        square = random.choice(board.get_empty_squares())
        board.move(square[0], square[1], player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    pass


def get_best_move(board, scores):
    empty = board.get_empty_squares()
    max_score = max([scores[r][c] for r, c in empty])
    moves = [(r, c) for r, c in empty if scores[r][c] == max_score]
    return random.choice(moves)


def mc_move(board, player, trials):
    pass


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)