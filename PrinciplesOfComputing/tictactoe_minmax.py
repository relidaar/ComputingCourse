"""
Mini-max Tic-Tac-Toe Player
"""
import random
import poc_ttt_gui
import poc_ttt_provided as provided
import codeskulptor

# try:
#     import poc_ttt_gui
#     import poc_ttt_provided as provided
#     import codeskulptor
# except ImportError:
#     from libs import poc_ttt_gui
#     import libs.poc_ttt_provided as provided
#     from SimpleGUICS2Pygame import codeskulptor

# Set timeout, as mini-max can take a long time
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    game_result = board.check_win()
    if game_result:
        return SCORES[game_result], (-1, -1)

    moves = dict()
    for move in board.get_empty_squares():
        current_board = board.clone()
        current_board.move(move[0], move[1], player)
        result = mm_move(current_board, provided.PLAYERX if player == provided.PLAYERO else provided.PLAYERO)
        moves[move] = result[0]

    best_move = max(moves.items(), key=lambda item: item[1] * SCORES[player])
    return best_move[1], best_move[0]


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
