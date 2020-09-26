"""
Student code for Word Wrangler game
"""

import urllib2
try:
    import codeskulptor
    import poc_wrangler_provided as provided
except ImportError:
    from SimpleGUICS2Pygame import codeskulptor
    import libs.poc_wrangler_provided as provided

WORD_FILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result = []
    for item in list1:
        if item not in result:
            result.append(item)
    return result


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    result = []
    list1 = list(list1)
    list2 = list(list2)
    while list1 and list2:
        if list1[0] <= list2[0]:
            result.append(list1[0])
            list1 = list1[1:]
        else:
            result.append(list2[0])
            list2 = list2[1:]
    return result + list1 + list2


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    length = len(list1)
    if not list1:
        return list1
    if length == 1:
        return [list1[0]]

    left = merge_sort(list1[:length/2])
    right = merge_sort(list1[length/2:])

    return merge(left, right)


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return []


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORD_FILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)


# Uncomment when you are ready to try the game
# run()


