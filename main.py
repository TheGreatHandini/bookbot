from stats import get_word_number,count_characters,sort_dictionaries, sort_on

def get_book_text (path):
    # gets the text from the book and returns in a string
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_number(book_text)
    sorted_dict = sort_dictionaries(count_characters(book_text))
    print('''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------''')
    for i in sorted_dict:
        print(i)
    print("============= END ===============")

main()