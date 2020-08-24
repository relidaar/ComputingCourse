import math

from libs.combinatorics import gen_permutations, gen_combinations, gen_all_sequences, gen_sorted_sequences

print '--Task 1--'
outcomes = ['Tails', 'Heads']
length = 5
print len(outcomes) ** length

print '\n--Task 2--'
outcomes = range(1, 5)
sequences = gen_all_sequences(outcomes, 2)
count = len(sequences)
products = [f * s for f, s in sequences]
sorted_products = sorted(set(products))
possibilities = [products.count(product) / float(count) for product in sorted_products]
print sum(product * possibility for product, possibility in zip(sorted_products, possibilities))

print '\n--Task 3--'
outcomes = range(10)
length = 5
sequences = gen_all_sequences(outcomes, length)
expected = 2 * len([i for i in range(len(outcomes)) if i + length <= len(outcomes)])
print expected / float(len(sequences))

print '\n--Task 4--'
outcomes = range(10)
length = 5
sequences = gen_permutations(outcomes, length)
expected = 2 * len([i for i in range(len(outcomes)) if i + length <= len(outcomes)])
print expected / float(len(sequences))

print '\n--Task 5--'
outcome = {"a", "b", "c", "d", "e", "f"}
permutations = gen_permutations(outcome, 4)
permutation_list = list(permutations)
permutation_list.sort()
print permutation_list[100]

print '\n--Task 6--'
outcomes = {1, 2}
subsets = []
for i in range(len(outcomes) + 1):
    for subset in gen_permutations(outcomes, i):
        subsets.append(subset)
print subsets

print '\n--Task 7--'
for value in range(3):
    outcomes = range(1, value + 1)
    subsets = []
    print 'outcomes:', outcomes
    for i in range(len(outcomes) + 1):
        for subset in gen_combinations(outcomes, i):
            subsets.append(subset)
    print 'subsets:', subsets

print '\n--Task 8--'
single_suit = float(math.factorial(13)) / (math.factorial(5) * math.factorial(8))
combinations = float(math.factorial(52)) / (math.factorial(5) * math.factorial(47))
print single_suit * 4 / combinations

print '\n--Task 9--'


def next_line(current_line):
    """
    Given a line in Pascal's triangle, generate the following line
    """
    result = [1]
    for idx in range(len(current_line) - 1):
        result.append(current_line[idx] + current_line[idx + 1])
    result.append(1)
    return result


TRIANGLE_HEIGHT = 5
pascal_line = [1]  # row zero
print pascal_line
for _ in range(TRIANGLE_HEIGHT - 1):
    pascal_line = next_line(pascal_line)
    print pascal_line
