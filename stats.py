def get_num_words(book): 
    words = book.split()
    count = 0
    
    for word in words:
        count += 1

    return f"Found {count} total words" 

def get_num_chars(book):
    content = book.split(" ")
    chars = {}
    for word in content:
        words = word.lower()
        for char in words:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

    return chars

def dict_to_dict_list(char_dict):
    sorted_char_list = [] 
    for char in char_dict:
        if not char.isalpha():
            continue
        newdict = {"char": char, "num": char_dict[char]}
        sorted_char_list.append(newdict)

    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list

def sort_on(dict):
    return dict["num"]
