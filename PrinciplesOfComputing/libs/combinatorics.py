def gen_all_sequences(outcomes, length):
    result = {()}
    for _ in range(length):
        temp = set()
        for seq in result:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        result = temp
    return result


def gen_sorted_sequences(outcomes, length):
    sequences = gen_all_sequences(outcomes, length)
    return set([tuple(sorted(item)) for item in sequences])


def gen_permutations(outcomes, length):
    result = {()}
    for _ in range(length):
        temp = set()
        for seq in result:
            for item in outcomes:
                if item in seq:
                    continue
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        result = temp
    return result


def gen_combinations(outcomes, length):
    permutations = gen_permutations(outcomes, length)
    return set([tuple(sorted(item)) for item in permutations])


outcomes = ['Red', 'Green', 'Blue']
length = 3
print 'outcomes (length of %d):' % length, outcomes
sequences = gen_all_sequences(outcomes, length)
sorted_sequences = gen_sorted_sequences(outcomes, length)
permutations = gen_permutations(outcomes, length)
combinations = gen_combinations(outcomes, length)
print '\nsequences (length of %d):' % len(sequences), sequences
print '\nsorted sequences (length of %d):' % len(sorted_sequences), sorted_sequences
print '\npermutations (length of %d):' % len(permutations), permutations
print '\ncombinations (length of %d):' % len(combinations), combinations
