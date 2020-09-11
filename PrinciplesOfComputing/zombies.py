"""
Student portion of Zombie Apocalypse mini-project
"""

import random

try:
    import poc_grid
    import poc_queue
    import poc_zombie_gui
except ImportError:
    from libs import poc_grid
    from libs import poc_queue
    from libs import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        self._zombie_list = list(zombie_list) if zombie_list is not None else []
        self._human_list = list(human_list) if human_list is not None else []

    def __str__(self):
        return 'Grid: \n%s' \
               'Humans: %s\n' \
               'Zombies %s\n' % (poc_grid.Grid.__str__(self), self._human_list, self._zombie_list)

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                self.set_empty(row, col)
        self._human_list = []
        self._zombie_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        return (zombie for zombie in self._zombie_list)

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        return (human for human in self._human_list)

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        width = self.get_grid_width()
        height = self.get_grid_height()

        boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            for zombie in self._zombie_list:
                boundary.enqueue(zombie)
        else:
            for human in self._human_list:
                boundary.enqueue(human)
        distance_field = [[width * height for _ in range(width)] for _ in range(height)]

        visited = poc_grid.Grid(height, width)
        for row in range(height):
            for col in range(width):
                if (row, col) in boundary:
                    visited.set_full(row, col)
                    distance_field[row][col] = 0
                elif not self.is_empty(row, col):
                    visited.set_full(row, col)
                else:
                    visited.set_empty(row, col)

        while boundary:
            current_cell = boundary.dequeue()
            for neighbor_cell in visited.four_neighbors(current_cell[0], current_cell[1]):
                if visited.is_empty(neighbor_cell[0], neighbor_cell[1]):
                    visited.set_full(neighbor_cell[0], neighbor_cell[1])
                    boundary.enqueue(neighbor_cell)
                    distance_field[neighbor_cell[0]][neighbor_cell[1]] = \
                        distance_field[current_cell[0]][current_cell[1]] + 1

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for index, human in enumerate(self._human_list):
            cells = self.eight_neighbors(human[0], human[1])
            cells = filter(lambda item: self.is_empty(item[0], item[1]), cells)
            cells.append(human)
            cells = [(cell, zombie_distance_field[cell[0]][cell[1]]) for cell in cells]
            self._human_list[index] = max(cells, key=lambda item: item[1])[0]

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for index, zombie in enumerate(self._zombie_list):
            cells = self.four_neighbors(zombie[0], zombie[1])
            cells = filter(lambda item: self.is_empty(item[0], item[1]), cells)
            cells.append(zombie)
            cells = [(cell, human_distance_field[cell[0]][cell[1]]) for cell in cells]
            self._zombie_list[index] = min(cells, key=lambda item: item[1])[0]

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))
