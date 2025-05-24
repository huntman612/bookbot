def sort_on(dict):
    return dict["num"]

def get_book_length(book):
    char_count = {}
    book_text = ""
    with open(book) as f:
        book_text = f.read()
    lower = book_text.lower()
    characters = list(lower)
    for character in characters:
        if character.isalpha():
            if character in char_count:
                char_count[character] += 1
            else:
                char_count[character] = 1
    return char_count


def get_word_count(book):
    book_text = ""
    with open(book) as f:
        book_text = f.read()
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_sorted_count(dict):
    listed_keys = list(dict)
    labelled_count = []
    sorted_count = {}
    for i in range(len(listed_keys)):
        labelled_dict = {}
        labelled_dict["char"] = listed_keys[i]
        labelled_dict["num"] = dict[listed_keys[i]]
        labelled_count.append(labelled_dict)
    labelled_count.sort(reverse=True, key=sort_on)
    for i in range(len(labelled_count)):
        temp_dict = {}
        temp_dict = labelled_count[i]
        sorted_count[temp_dict["char"]] = temp_dict["num"]
    return sorted_count