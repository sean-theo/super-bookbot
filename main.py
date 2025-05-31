from stats import word_count, character_count, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    directory = character_count(text)
    print(f"{word_count(text)} words found in the document")
    sort_dictionary(directory)
    
main()

