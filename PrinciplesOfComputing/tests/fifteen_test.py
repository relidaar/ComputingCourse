import unittest
from .. import fifteen_puzzle


class TestFifteenPuzzle(unittest.TestCase):
    def test_initial_position_invariant_negative(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._initial_position_invariant(-1, 0), False)
        self.assertEqual(puzzle._initial_position_invariant(3, 0), False)
        self.assertEqual(puzzle._initial_position_invariant(0, -1), False)
        self.assertEqual(puzzle._initial_position_invariant(0, 3), False)

    def test_initial_position_invariant_positive(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._initial_position_invariant(0, 0), True)

    def test_correct_position_invariant_negative(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._correct_position_invariant(0, 0), False)

    def test_correct_position_invariant_positive(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._correct_position_invariant(1, 2), True)

    def test_zero_position_invariant_negative(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._zero_position_invariant(0, 0), False)

    def test_zero_position_invariant_positive(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._zero_position_invariant(1, 1), True)

    def test_row_positions_invariant_negative(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._row_positions_invariant(0, 0), False)

    def test_row_positions_invariant_positive(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._row_positions_invariant(2, 0), True)

    def test_lower_rows_positions_invariant_negative(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._lower_rows_positions_invariant(0), False)

    def test_lower_rows_positions_invariant_positive(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle._lower_rows_positions_invariant(1), True)

    def test_lower_row_invariant_negative(self):
        grid = [
            [5, 7, 1],
            [4, 0, 2],
            [6, 3, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle.lower_row_invariant(1, 1), False)

    def test_lower_row_invariant_positive(self):
        grid = [
            [2, 3, 1],
            [4, 0, 5],
            [6, 7, 8]
        ]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle.lower_row_invariant(1, 1), True)

    def test_lower_row_invariant(self):
        grid = [
            [15, 11, 10, 9, 8],
            [7, 6, 5, 4, 3],
            [2, 1, 0, 13, 14],
            [12, 16, 17, 18, 19]]
        puzzle = fifteen_puzzle.Puzzle(len(grid), len(grid[0]), grid)
        self.assertEqual(puzzle.lower_row_invariant(2, 2), False)

