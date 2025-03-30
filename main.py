from stats import count_words
from stats import count_characters
from stats import sort_characters

import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    sorted_characters = sort_characters(num_characters)



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_characters:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()