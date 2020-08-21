"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
try:
    import poc_ttt_gui
    import poc_ttt_provided as provided
except ImportError:
    import libs.poc_ttt_gui as poc_ttt_gui
    import libs.poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player


# Add your functions here.
def mc_trial(board, player):
    while not board.check_win():
        move = random.choice(board.get_empty_squares())
        board.move(move[0], move[1], player)
        player = provided.PLAYERX if player == provided.PLAYERO else provided.PLAYERO


def mc_update_scores(scores, board, player):
    pass


def get_best_move(board, scores):
    pass


def mc_move(board, player, trials):
    dim = range(board.get_dim())
    scores = [[0 for _ in dim] for _ in dim]
    current_board = board.clone()
    for _ in range(trials):
        current_board = board.clone()
        mc_trial(current_board, player)
        mc_update_scores(scores, current_board, player)
    return get_best_move(current_board, scores)


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
