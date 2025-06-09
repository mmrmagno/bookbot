import sys
from stats import get_num_words
from stats import get_num_chars
from stats import dict_to_dict_list

def get_book_text(filepath):
    with open(filepath) as book:
        out = book.read()
        return out 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    word_count = get_num_words(get_book_text(book_path))
    char_count = dict_to_dict_list(get_num_chars(get_book_text(book_path)))
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path} 
----------- Word Count ----------
{word_count}
--------- Character Count -------""")
    
    for i in range(0, len(char_count)):
        print(f"{char_count[i]["char"]}: {char_count[i]["num"]}")

    print("============= END ===============")

main()
