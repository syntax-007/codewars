def tower_builder(n_floors):
    pyramid = []
    if n_floors > 0:
        num_of_spaces = (n_floors * 2) - 1
        for floor in range(1, num_of_spaces + 1, 2):
            stars_string = "*" * floor
            pyramid.append(stars_string.center(num_of_spaces))

    return pyramid


print(tower_builder(7))
