"""
Merge function for 2048 game.
"""


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
