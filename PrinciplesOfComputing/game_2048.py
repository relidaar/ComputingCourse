"""
Clone of 2048 game.
"""

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def arrange(line):
    '''
    Function that moves all zeros to the end of line.
    :param line: collection of numbers
    :return: arranged line with trailing zeros
    '''
    return [num for num in line if num != 0] + [num for num in line if num == 0]


def merge_equal(line):
    '''
    Function that merges and doubles identical adjacent numbers (if not zeros).
    :param line: collection of numbers
    :return: arranged line with merged identical numbers
    '''
    temp = []
    size = len(line)
    index = 0
    while index < size:
        current = line[index]
        if index + 1 >= size:
            temp.append(current)
            break
        if current == line[index + 1] and current != 0:
            temp.append(current * 2)
            index += 2
        else:
            temp.append(current)
            index += 1
    return temp


def add_trailing_zeros(line, expected_size):
    '''
    Function that adds trailing zeros.
    :param line: collection of numbers
    :param expected_size: expected size of result line
    :return: line of expected size with trailing zeros
    '''
    temp = list(line)
    while len(temp) < expected_size:
        temp.append(0)
    return temp


def merge(line):
    '''
    Function that merges a single row or column in 2048.
    :param line: collection of numbers
    :return: merged 2048 line
    '''
    result = arrange(line)
    result = merge_equal(result)
    result = add_trailing_zeros(result, len(line))
    return result


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._width = grid_width
        self._height = grid_height
        self._board = [[]]
        self.reset()
        self._initial_tiles = {
            UP: [(0, col) for col in range(grid_width)],
            DOWN: [(grid_height - 1, col) for col in range(grid_width)],
            LEFT: [(row, 0) for row in range(grid_height)],
            RIGHT: [(row, grid_width - 1) for row in range(grid_height)],
        }

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[0 for _ in range(self._width)] for _ in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        board = ""
        for row in range(self._height):
            board += '\n'
            for col in range(self._width):
                board += str(self._board[row][col])
        return board

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        offset = OFFSETS[direction]
        init = self._initial_tiles[direction]
        changed = False
        for initial_tile in init:
            row = initial_tile[0]
            col = initial_tile[1]
            line = []
            while 0 <= row < self._height and 0 <= col < self._width:
                line.append(self.get_tile(row, col))
                row += offset[0]
                col += offset[1]
            line = merge(line)
            row = initial_tile[0]
            col = initial_tile[1]
            index = 0
            while 0 <= row < self._height and 0 <= col < self._width:
                if self._board[row][col] != line[index]:
                    changed = True
                self._board[row][col] = line[index]
                row += offset[0]
                col += offset[1]
                index += 1
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_tiles = [(row, col) for col in range(self._width) for row in range(self._height)
                       if self.get_tile(row, col) == 0]
        pos = random.choice(empty_tiles)
        if random.randint(1, 10) < 10:
            self._board[pos[0]][pos[1]] = 2
        else:
            self._board[pos[0]][pos[1]] = 4

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        if 0 <= row < self._height and 0 <= col < self._width:
            self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        if 0 <= row < self._height and 0 <= col < self._width:
            return self._board[row][col]

# try:
#     import poc_2048_gui
# except ImportError:
#     from libs import poc_2048_gui
# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
