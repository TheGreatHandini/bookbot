def get_book_text (path):
    # gets the text from the book and returns in a string
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print (book_text)

main()