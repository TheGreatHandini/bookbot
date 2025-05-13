from stats import get_word_number
from stats import count_characters

def get_book_text (path):
    # gets the text from the book and returns in a string
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_number(book_text)
    print(f'{word_count} words found in the document')
    print(count_characters(book_text))

main()