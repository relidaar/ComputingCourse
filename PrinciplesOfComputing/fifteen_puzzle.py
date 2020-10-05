"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid is not None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return row, col
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def _initial_position_invariant(self, initial_row, initial_col):
        """
        Check if the position is in boundaries
        """
        return (0 <= initial_row < self._height) and (0 <= initial_col < self._width)

    def _correct_position_invariant(self, row, col):
        """
        Check if the tile on the provided position has correct value
        """
        return self.get_number(row, col) == row * self._width + col

    def _zero_position_invariant(self, initial_row, initial_col):
        """
        Check if value of the tile on the provided position is zero
        """
        return self.get_number(initial_row, initial_col) == 0

    def _row_positions_invariant(self, initial_row, initial_col=0):
        """
        Check if the all tiles of the row from initial column have correct values
        """
        for col in range(initial_col, self._width):
            if not self._correct_position_invariant(initial_row, col):
                return False
        return True

    def _lower_rows_positions_invariant(self, initial_row):
        """
        Check if the all tiles of lower rows from initial column have correct values
        """
        for row in range(initial_row + 1, self._height):
            if not self._row_positions_invariant(row):
                return False
        return True

    def lower_row_invariant(self, initial_row, initial_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (initial_row > 1)
        Returns a boolean
        """
        return self._initial_position_invariant(initial_row, initial_col) and \
               self._zero_position_invariant(initial_row, initial_col) and \
               self._row_positions_invariant(initial_row, initial_col + 1) and \
               self._lower_rows_positions_invariant(initial_row)

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, target_col)
        row, col = self.current_position(target_row, target_col)
        moves = move(target_row, target_col, row, col)
        self.update_puzzle(moves)
        assert self.lower_row_invariant(target_row, target_col - 1)
        return moves

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0)
        row, col = self.current_position(target_row, 0)
        moves = 'ur'
        if row == target_row - 1 and col == 0:
            moves += 'r' * (self._width - 2)
            self.update_puzzle(moves)
            return moves
        moves += move(target_row - 1, 1, row, col) + 'ruldrdlurdluurddlur' + 'r' * (self._width - 2)
        self.update_puzzle(moves)
        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1)
        return moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        return self._zero_position_invariant(0, target_col) and \
               self._row_positions_invariant(1, target_col) and \
               self._lower_rows_positions_invariant(1)

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        return self.lower_row_invariant(1, target_col)

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        self.row0_invariant(target_col)
        row, col = self.current_position(0, target_col)
        moves = 'ld'
        if row == 0 and col == target_col - 1:
            self.update_puzzle(moves)
            return moves
        moves += move(1, target_col - 1, row, col) + 'urdlurrdluldrruld'
        self.update_puzzle(moves)
        self.row0_invariant(target_col)
        return moves

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        self.row1_invariant(target_col)
        row, col = self.current_position(1, target_col)
        moves = move(1, target_col, row, col)
        moves += 'ur'
        self.update_puzzle(moves)
        self.row1_invariant(target_col)
        return moves

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""


def move(target_row, target_col, row, col):
    '''
    Moves a tile from (row, col) to (target row, target col)
    '''
    moves = ''
    vertical_turn = 'druld'
    horizontal_right_turn = 'rdllu' if row == 0 else 'rulld'
    horizontal_left_turn = 'drrul' if row == 0 else 'urrdl'

    horizontal_delta = target_col - col
    vertical_delta = target_row - row
    moves += 'u' * vertical_delta
    if horizontal_delta == 0:
        moves += 'ld' + vertical_turn * (vertical_delta - 1)
    elif horizontal_delta < 0:
        moves += 'r' * (abs(horizontal_delta) - 1) + horizontal_right_turn * abs(horizontal_delta)
    elif horizontal_delta > 0:
        moves += 'l' * horizontal_delta + horizontal_left_turn * (horizontal_delta - 1)
    moves += vertical_turn * vertical_delta
    return moves


# Start interactive simulation
# try:
#     import poc_fifteen_gui
# except ImportError:
#     from libs import poc_fifteen_gui
#
# obj = Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]])
# poc_fifteen_gui.FifteenGUI(obj)
# poc_fifteen_gui.FifteenGUI(Puzzle(2, 2))
