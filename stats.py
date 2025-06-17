
def char_count(book_text):
    lower_c = book_text.lower()
    char_dict = {}

    for char in lower_c:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def sort_count(dict):
    return dict["num"]

def list_of_dicts(char_dict):
    char_list = []

    for letter, time_counted in char_dict.items():
        char_list.append({"char": letter, "num": time_counted})
    char_list.sort(reverse=True, key=sort_count)

    return char_list

def word_count(book_text):
    book_text = book_text.split()
    wc = 0
    for i in book_text:
        wc += 1
    return wc