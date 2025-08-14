from stats import get_num_words
from stats import get_num_characters
from stats import report
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def get_num_words(filepath):
    words = []
    with open(filepath) as file:
        words = file.read()
        return len(words.split())

def main():
    if len(sys.argv) == 2:
        book_location = sys.argv[1]
        text = get_book_text(book_location)
        num_words = get_num_words(book_location)
        words = get_num_characters(text)
        char_dict = report(words)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_location}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for character in char_dict:
            letter = character["char"]
            number = character["num"]
            print(f"{letter}: {number}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
