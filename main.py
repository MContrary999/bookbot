import sys
from stats import get_num_words, each_character, sorted_char

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    chars_dict = each_character(text)
    count = get_num_words(text)
    char_list = sorted_char(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char in char_list:
        if char["char"].isalpha() == True:
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    
main()