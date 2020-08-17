"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.board = [0]

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.board = list(configuration)

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self.board[::-1])

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        return self.board[0] != 0 and all(x == 0 for x in self.board[1:])

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        return 0 < house_num < len(self.board) and self.board[house_num] > 0

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            seeds = self.board[house_num]
            self.board[house_num] = 0
            index = house_num - 1
            while seeds > 0 and index >= 0:
                self.board[index] += 1
                seeds -= 1
                index -= 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house_num in enumerate(self.board):
            if self.is_legal_move(house_num):
                return house_num
        return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
        After each move, move the seeds in the house closest
        to the store when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        moves = []
        while not self.is_game_won():
            house_num = self.choose_move()
            if self.is_legal_move(house_num):
                self.apply_move(house_num)
                moves.append(house_num)
        return moves


# Import GUI code once you feel your code is correct

try:
    import poc_mancala_gui
    import mancala_test
except ImportError:
    from libs import poc_mancala_gui
    from tests import mancala_test

# poc_mancala_gui.run_gui(SolitaireMancala())
mancala_test.run_suite(SolitaireMancala)
