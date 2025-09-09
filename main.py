def get_book_text(filepath):
        with open(filepath) as f:
           text = f.read()
        return text
def main():
         content = get_book_text("./books/frankenstein.txt")
         print (content)
        
main()
