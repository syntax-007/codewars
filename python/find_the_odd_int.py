def find_it(seq):
    unique_values = set(seq)
    odd_number_of_times = 0
    for value in unique_values:
        counter = 0
        for digit in seq:
            if value == digit:
                counter += 1

        if counter % 2 != 0:
            odd_number_of_times = value

    return odd_number_of_times


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
