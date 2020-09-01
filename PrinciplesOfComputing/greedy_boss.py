"""
Simulator for greedy boss scenario
"""

import math

try:
    import simpleplot
    import codeskulptor
except ImportError:
    from SimpleGUICS2Pygame import simpleplot
    from SimpleGUICS2Pygame import codeskulptor

codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


class Bribe:
    def __init__(self, cost_increment):
        self._cost = INITIAL_BRIBE_COST
        self._cost_increment = cost_increment

    def get_cost(self):
        return self._cost

    def update_cost(self):
        self._cost += self._cost_increment


class Worker:
    def __init__(self):
        self._current_day = 0
        self._total_earnings = 0
        self._current_earnings = 0
        self._salary_per_day = INITIAL_SALARY

    def get_current_day(self):
        return self._current_day

    def get_earnings(self):
        return self._current_earnings

    def get_total_earnings(self):
        return self._total_earnings

    def days_to_next_bribe(self, bribe_cost):
        if self._current_earnings >= bribe_cost:
            return 0
        return int(math.ceil((bribe_cost - self._current_earnings) / float(self._salary_per_day)))

    def wait(self, days_to_wait):
        if 0 < days_to_wait:
            self._current_day += days_to_wait
            earnings = self._salary_per_day * days_to_wait
            self._current_earnings += earnings
            self._total_earnings += earnings

    def pay_bribe(self, bribe):
        self._current_earnings -= bribe.get_cost()
        self._salary_per_day += SALARY_INCREMENT
        bribe.update_cost()


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    """
    Simulation of greedy boss
    """

    # initialize necessary local variables
    current_day = 0

    # define  list consisting of days vs. total salary earned for analysis
    days_vs_earnings = []

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        pass
        # update list with days vs total salary earned
        # use plot_type to control whether regular or log/log plot

        # check whether we have enough money to bribe without waiting

        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)

        # update state of simulation to reflect bribe

    return days_vs_earnings


def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = STANDARD
    days = 70
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings",
                          [inc_0, inc_500, inc_1000, inc_2000], False,
                          ["Bribe increment = 0", "Bribe increment = 500",
                           "Bribe increment = 1000", "Bribe increment = 2000"])


run_simulations()

print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]




