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

def sort_on(dict):
    return dict["num"]

def sort_dictionaries(character_dict):
    dictionary_list =[]
    for key,value in character_dict.items():
        new_dict = {"char": key, "num": value}
        dictionary_list.append(new_dict)
    dictionary_list.sort(reverse=True, key=sort_on )
    return dictionary_list
