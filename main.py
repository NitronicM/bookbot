from stats import get_num_words
from stats import get_book_text
from stats import character_breakdown
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    print(f"""  ============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
{get_num_words(content)}
--------- Character Count -------""")
    tracker = character_breakdown(content)
    for key in tracker:
        print(f"{key}: {tracker[key]}")


main()

