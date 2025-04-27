from stats import get_num_words, get_character_counts, sort_characters
import sys

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
    if len(sys.argv) == 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    filepath = sys.argv[1]
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
