def find_it(seq):
    unique = set(seq)
    return_value = {}
    odd_number = 0

    for num in unique:
        return_value[num] = seq.count(num)

    print(return_value)
    for key in return_value.keys():
        if return_value[key] % 2 != 0 and return_value[key] > odd_number:
            odd_number = key

    return odd_number


def test_find_it():
    assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
    assert find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
    assert find_it([10, 10, 10]) == 10
    assert find_it([10]) == 10
    assert find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1