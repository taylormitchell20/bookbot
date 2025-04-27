def get_num_words(book):
    words = book.split()
    return len(words)

def get_character_counts(book):
    characters = {}
    for char in book:
        lower_char = char.lower()
        if lower_char not in characters:
            characters[lower_char] = 1
        else:
            characters[lower_char] += 1
    return characters

def sort_characters(characters):
    char_list = []
    for char in characters:
        char_list.append({'char': char, 'num': characters[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict['num']
