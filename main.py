import sys
from stats import *
from plots import *


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as bookfile:
        return bookfile.read()


def main():
    plot = decision()
    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    num_words = find_words(text)
    character_count = characters(text)
    make_pretty(num_words, character_count)
    if plot:
        plotting(text)


if __name__ == "__main__":
    main()
