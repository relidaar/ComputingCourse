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
