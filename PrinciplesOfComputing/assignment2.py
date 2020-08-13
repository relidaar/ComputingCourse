"""
Clone of 2048 game.
"""

import libs.poc_2048_gui as poc_2048_gui
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


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    temp = [x for x in line if x != 0] + [x for x in line if x == 0]

    result = []
    index = 0
    size = len(temp)
    while index < size:
        if index + 1 >= size:
            result.append(temp[index])
            break
        if temp[index] == temp[index + 1]:
            result.append(temp[index] * 2)
            index += 2
        else:
            result.append(temp[index])
            index += 1

    out = [0] * len(line)
    out[:len(result)] = result
    return out


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid = []
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.reset()
        self.initial_tiles = {
            UP: [(0, c) for c in range(self.grid_width)],
            DOWN: [(self.grid_height - 1, c) for c in range(self.grid_width)],
            LEFT: [(r, 0) for r in range(self.grid_height)],
            RIGHT: [(r, self.grid_width - 1) for r in range(self.grid_height)],
        }

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = []
        for row in range(self.grid_height):
            self.grid.append([])
            for _ in range(self.grid_width):
                self.grid[row].append(0)
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return_string = ""
        for row in range(self.grid_height):
            return_string += '\n'
            for col in range(self.grid_width):
                return_string += str(self.grid[row][col])
        return return_string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        offset = OFFSETS[direction]
        init = self.initial_tiles[direction]
        changed = False
        for tile in init:
            temp = []
            row = tile[0]
            col = tile[1]
            while 0 <= row < self.grid_height and 0 <= col < self.grid_width:
                temp.append(self.grid[row][col])
                row += offset[0]
                col += offset[1]
            temp = merge(temp)
            index = 0
            row = tile[0]
            col = tile[1]
            while 0 <= row < self.grid_height and 0 <= col < self.grid_width:
                if self.grid[row][col] != temp[index]:
                    changed = True
                self.grid[row][col] = temp[index]
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
        row = random.randrange(self.grid_height)
        col = random.randrange(self.grid_width)

        while self.grid[row][col] != 0:
            row = random.randrange(self.grid_height)
            col = random.randrange(self.grid_width)

        self.grid[row][col] = 4 if random.randint(1, 100) >= 90 else 2

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
