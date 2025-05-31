def word_count(words):
    split_text = words.split()
    return len(split_text)

def character_count(words):
    dictionary = {}
    lowercase_book = words.lower()
    for a in lowercase_book:
        if a not in dictionary:
            dictionary[a] = 1
        else:
            dictionary[a] += 1
    return dictionary
    
def sort_dictionary(dict):   
    return dict["num"]