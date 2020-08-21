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
    '''
    Simulates a TicTacToe game
    :param board: game board
    :param player: current player
    :return: None
    '''
    while not board.check_win():
        move = random.choice(board.get_empty_squares())
        board.move(move[0], move[1], player)
        provided.switch_player(player)


def mc_update_scores(scores, board, player):
    '''
    Updates total scores
    :param scores: total scores
    :param board: game board
    :param player: current player
    :return: None
    '''
    other = provided.PLAYERO if player == provided.PLAYERX else provided.PLAYERX
    if player == board.check_win():
        score_current = SCORE_CURRENT
        score_other = -SCORE_OTHER
    else:
        score_current = -SCORE_CURRENT
        score_other = SCORE_OTHER
    dim = board.get_dim()
    for row in range(dim):
        for col in range(dim):
            square = board.square(row, col)
            if square == player:
                scores[row][col] += score_current
            if square == other:
                scores[row][col] += score_other


def get_best_move(board, scores):
    pass


def mc_move(board, player, trials):
    '''
    Uses Monte Carlo method for calculating the best move
    :param board: game board
    :param player: current player
    :param trials: number of trials to do
    :return: indices (row, col) of board square as move
    '''
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
