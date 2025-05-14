from stats import get_word_number,count_characters,sort_dictionaries, sort_on
import sys

def get_book_text (path):
    # gets the text from the book and returns in a string
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:  
        book_text = get_book_text(sys.argv[1])
        word_count = get_word_number(book_text)
        sorted_dict = sort_dictionaries(count_characters(book_text))
        print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
        for i in sorted_dict:
            print(f'{i['char']}: {i['num']}')
        print("============= END ===============")


if __name__ == "__main__":
    main()