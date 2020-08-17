"""
Template for testing suite for Solitaire Mancala
"""

try:
    import poc_simpletest
except ImportError:
    from PrinciplesOfComputing.libs import poc_simpletest


def run_suite(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    game = game_class()

    suite.run_test(str(game), str([0]), 'Test #0: init')
    config1 = [0, 0, 1, 1, 3, 5, 0]
    game.set_board(config1)
    suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1a: str")
    suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
    suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
    suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")

    # report number of tests and failures
    suite.report_results()
