def get_word_number(book_text):
    word_list = book_text.split()
    word_number = len(word_list)
    return word_number

def count_characters(book_text):
    book_text = book_text.lower()
    letter_dictionary ={}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        letter_count = book_text.count(letter)
        letter_dictionary[letter] = letter_count
    return letter_dictionary
