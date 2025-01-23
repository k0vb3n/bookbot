def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    
    text = book_opener(book_path)
    num_words = word_counter(text)
    chars_dict = character_counter(text)
    chars_list = dictionary_to_list(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)

    #print(chars_list)
    #print(chars_dict)
    print(f"{num_words} words found in the document\n")

    for chars in chars_list:
        print(f"The '{chars["character"]}' character was found {chars["count"]} times")


def character_counter(book):
    characters = {}
    for character in book:
        if character.isalpha():
            lowered = character.lower()
            if lowered in characters:
                characters[lowered] += 1
            else:
                characters[lowered] = 1
    return characters

def word_counter(book):
    words = book.split()
    return len(words)

def book_opener(file_path):
    with open(file_path) as f:
        return f.read()

def dictionary_to_list(dict):
    list_dict = []
    for lines in dict:
        temp = {}
        temp["character"] = lines
        temp["count"] = dict[lines]
        list_dict.append(temp)
    return list_dict

def sort_on(dict):
    return dict["count"]

main()