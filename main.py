

def get_book_text(filepath):
        with open(filepath) as f:
           text = f.read()
        return text
        
from stats import get_num_words

def main():
        content = get_book_text("./books/frankenstein.txt")
        num_words = get_num_words(content) 
        print (f"{num_words} words found in the document")     
main()
