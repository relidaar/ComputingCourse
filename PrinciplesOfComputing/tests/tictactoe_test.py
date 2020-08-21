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
from .. import tictactoe


class Test2048Game(unittest.TestCase):
    def test_game_trial(self):
        board = provided.TTTBoard(3)
        player = provided.PLAYERO
        tictactoe.mc_trial(board, player)
        self.assertIsNotNone(board.check_win())


def run_suite(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game

    # report number of tests and failures
    suite.report_results()
