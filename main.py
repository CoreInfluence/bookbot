#!/usr/bin/env python3

from stats import get_num_words

def get_book_test(bookname):
    book_path = f"books/{bookname}.txt"
    # print(book_path)
    with open(book_path,"r") as book:
        book_contents = book.read()
        return book_contents

def main():
    #print(get_book_test("frankenstein"))
    print(f"{get_num_words('frankenstein')} words found in the document")



if __name__ == '__main__':
    main()