from stats import word_count
from stats import character_count
from stats import dictionary_sort
import sys


def get_book_text(filepath):

    read_text = ""

    with open(filepath) as f:
        read_text = f.read()

    return read_text


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        word_totals = word_count(text)
        char_counts = character_count(text)
        sorted_chars = dictionary_sort(char_counts)


    

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print("Found", word_totals, "total words")
        print("--------- Character Count -------")
        for char_dict in sorted_chars:
            print(f"{char_dict['char']}: {char_dict['count']}")
        print("============= END ===============")

main()