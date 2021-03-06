"""
Template for testing suite for TicTacToe
"""

try:
    import poc_simpletest
    import poc_ttt_gui
    import poc_ttt_provided as provided
except ImportError:
    from PrinciplesOfComputing.libs import poc_simpletest
    import PrinciplesOfComputing.libs.poc_ttt_gui as poc_ttt_gui
    import PrinciplesOfComputing.libs.poc_ttt_provided as provided
import unittest
from .. import tictactoe_montecarlo


class Test2048Game(unittest.TestCase):
    def test_game_trial(self):
        board = provided.TTTBoard(3)
        player = provided.PLAYERO
        tictactoe_montecarlo.mc_trial(board, player)
        self.assertIsNotNone(board.check_win())
        self.assertIn(board.check_win(), [provided.PLAYERO, provided.PLAYERX, provided.DRAW])

    def test_update_scores_player_won(self):
        dim = 3
        board = [
            [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
            [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX],
            [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]
        ]
        expected = [[0 for _ in range(dim)] for _ in range(dim)]
        for row in range(dim):
            for col, square in enumerate(board[row]):
                if square == provided.PLAYERO:
                    expected[row][col] += tictactoe_montecarlo.SCORE_CURRENT
                if square == provided.PLAYERX:
                    expected[row][col] -= tictactoe_montecarlo.SCORE_OTHER
        board = provided.TTTBoard(dim, False, board)
        scores = [[0 for _ in range(dim)] for _ in range(dim)]
        tictactoe_montecarlo.mc_update_scores(scores, board, provided.PLAYERO)
        self.assertEqual(expected, scores)

    def test_update_scores_player_lost(self):
        dim = 3
        board = [
            [provided.PLAYERX, provided.PLAYERO, provided.PLAYERO],
            [provided.PLAYERX, provided.PLAYERX, provided.EMPTY],
            [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX]
        ]
        expected = [[0 for _ in range(dim)] for _ in range(dim)]
        for row in range(dim):
            for col, square in enumerate(board[row]):
                if square == provided.PLAYERO:
                    expected[row][col] -= tictactoe_montecarlo.SCORE_CURRENT
                if square == provided.PLAYERX:
                    expected[row][col] += tictactoe_montecarlo.SCORE_OTHER
        board = provided.TTTBoard(dim, False, board)
        scores = [[0 for _ in range(dim)] for _ in range(dim)]
        tictactoe_montecarlo.mc_update_scores(scores, board, provided.PLAYERO)
        self.assertEqual(expected, scores)

    def test_get_best_move(self):
        board = [
            [provided.EMPTY, provided.PLAYERO, provided.EMPTY],
            [provided.PLAYERX, provided.EMPTY, provided.EMPTY],
            [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]
        ]
        board = provided.TTTBoard(len(board), False, board)
        scores = [
            [3, 1, 2],
            [-1, 3, 3],
            [2, 2, -1]
        ]
        moves = [(0, 0), (1, 2), (1, 3)]
        move = tictactoe_montecarlo.get_best_move(board, scores)
        self.assertIn(move, moves)


def run_suite(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game

    # report number of tests and failures
    suite.report_results()
