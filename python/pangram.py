alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z')


def is_pangram(text):
    count = 0
    for letter in alphabet:
        if tuple(text.lower()).__contains__(letter):
            count += 1

    print(count)
    return count >= len(alphabet)
