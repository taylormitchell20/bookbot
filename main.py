from stats import get_num_words, get_character_counts, sort_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(filepath, word_count, character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for character in character_list:
        char = character['char']
        num = character['num']
        if char.isalpha():
            print(f'{char}: {num}')
    print('============= END ===============')
    return

def main():
    filepath = 'books/frankenstein.txt'
    book = get_book_text(filepath)
    word_count = get_num_words(book)
    character_counts = get_character_counts(book)
    character_list = sort_characters(character_counts)
    print_report(filepath, word_count, character_list)
    return

def test1(string):
    char_counts = get_character_counts(string)
    char_list = sort_characters(char_counts)
    print(char_list)

main()
