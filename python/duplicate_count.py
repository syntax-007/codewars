def duplicate_count(text):
    number_of_duplicates = 0
    for letter in set(text.lower()):
        if text.lower().count(letter) > 1:
            number_of_duplicates += 1

    return number_of_duplicates
   
print(duplicate_count("abcdeaB"))