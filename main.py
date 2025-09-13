from stats import get_num_words 
from stats import count_characters
from stats import build_sorted_char_list


def get_book_text(filepath):
        with open(filepath) as f:
           text = f.read()
        return text
     
def main():
        content = get_book_text("./books/frankenstein.txt")
        num_words = get_num_words(content) 
        counts = count_characters(content)
        sorted_chars = build_sorted_char_list(counts)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print (f"Found {num_words} total words") 
        print("--------- Character Count -------")    
        for item in sorted_chars:
              print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
main()
