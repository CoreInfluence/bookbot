#!/usr/bin/env python3

def get_book_test(bookname):
    book_path = f"books/{bookname}.txt"
    # print(book_path)
    with open(book_path,"r") as book:
        book_contents = book.read()
        return book_contents

def get_number_of_words_in_book(bookname):
    book_path = f"books/{bookname}.txt"
    # print(book_path)
    with open(book_path,"r") as book:
        book_contents = book.read()
        book_contents_list = book_contents.split()
        return len(book_contents_list)
        # print(book_contents_list)

def main():
    #print(get_book_test("frankenstein"))
    print(f"{get_number_of_words_in_book('frankenstein')} words found in the document")



if __name__ == '__main__':
    main()