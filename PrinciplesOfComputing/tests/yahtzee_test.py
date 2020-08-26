"""
Template for testing suite for TicTacToe
"""

import unittest
from parameterized import parameterized
from .. import yahtzee


class TestYahtzee(unittest.TestCase):
    @parameterized.expand([
        [tuple([]), {()}],
        [tuple([2, 4]), {(), (2,), (4,), (2, 4)}],
        [tuple((1, 2, 2)), {(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)}],
        [tuple((3, 3, 3)), {(), (3,), (3, 3), (3, 3, 3)}],
        [tuple([2, 3, 6]), {(), (2,), (3,), (6,), (2, 3), (2, 6), (3, 6), (2, 3, 6)}],
    ])
    def test_gen_all_holds(self, hand, expected):
        """ Test addition. """
        self.assertEqual(yahtzee.gen_all_holds(hand), expected)

    @parameterized.expand([
        [tuple([]), 0],
        [tuple([2, 4]), 4],
        [tuple((1, 2, 2)), 4],
        [tuple((1, 1, 2)), 2],
        [tuple((3, 3, 3)), 9],
        [tuple((3, 3, 4)), 6],
        [tuple((3, 4, 4)), 8],
        [tuple([2, 3, 6]), 6],
    ])
    def test_score(self, hand, expected):
        """ Test addition. """
        self.assertEqual(yahtzee.score(hand), expected)
