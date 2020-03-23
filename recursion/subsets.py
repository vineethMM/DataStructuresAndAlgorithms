def all_subsets(in_set):
    if(len(in_set)) == 1:
        return [in_set]
    else:
        element = in_set.pop()
        # find all the subsets of remaining set
        subsets = all_subsets(in_set)
        # to find all the subsets
        # current `element` will be a subset
        # + subset of remaining set
        # + current element added to all the elements in subset of remaing set
        all_sets = [[element]] + subsets + [x + [element] for x in subsets]

        return  all_sets

if __name__ == "__main__":
    input = all_subsets([1, 2, 3])
    expected_output = [[3], [2], [1], [1, 2], [2, 3], [1, 3], [1, 2, 3]]
    actual_output   = all_subsets(input)
    assert set([set(x) for x in actual_output]) == set([set(x) for x in expected_output])
