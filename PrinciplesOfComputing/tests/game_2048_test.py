import unittest
from .. import game_2048


class Test2048Game(unittest.TestCase):
    def test_merge(self):
        self.assertEqual([2, 0, 0, 0], game_2048.merge([0, 2, 0, 0]))
        self.assertEqual([2, 0, 0, 0], game_2048.merge([0, 2, 0, 0]))
        self.assertEqual([2, 4, 0, 0], game_2048.merge([0, 2, 4, 0]))
        self.assertEqual([4, 0, 0, 0], game_2048.merge([0, 2, 2, 0]))
        self.assertEqual([2, 4, 0, 0], game_2048.merge([0, 2, 0, 4]))
        self.assertEqual([4, 0, 0, 0], game_2048.merge([0, 0, 0, 4]))
        self.assertEqual([2, 8, 4, 0], game_2048.merge([0, 2, 8, 4]))
        self.assertEqual([4, 0, 0, 0], game_2048.merge([0, 2, 0, 2]))

    def test_get_width_height(self):
        width, height = 4, 4
        game = game_2048.TwentyFortyEight(width, height)
        self.assertEqual(width, game.get_grid_width())
        self.assertEqual(height, game.get_grid_height())

    def test_get_set_tile(self):
        width, height = 4, 4
        game = game_2048.TwentyFortyEight(width, height)

        row, col, value = 0, 0, 2
        game.set_tile(row, col, value)
        self.assertEqual(value, game.get_tile(row, col))

    def test_reset(self):
        width, height = 4, 4
        game = game_2048.TwentyFortyEight(width, height)
        game.reset()
        empty = 0
        non_empty = 0
        for row in range(width):
            for col in range(height):
                if game.get_tile(row, col) == 0:
                    empty += 1
                if game.get_tile(row, col) > 0:
                    non_empty += 1
        self.assertEqual(width * height - 2, empty)
        self.assertEqual(2, non_empty)

    def test_str(self):
        width, height = 4, 4
        game = game_2048.TwentyFortyEight(width, height)
        for row in range(width):
            for col in range(height):
                game.set_tile(row, col, 1)
        expected = '1 1 1 1\n' \
                   '1 1 1 1\n' \
                   '1 1 1 1\n' \
                   '1 1 1 1\n'
        self.assertEqual(expected, str(game))
