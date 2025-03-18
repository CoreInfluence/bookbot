#!/usr/bin/env python3

import stats
import sys

def get_book_test(book_path):
    # book_path = f"books/{bookname}.txt"
    # print(book_path)
    with open(book_path,"r") as book:
        book_contents = book.read()
        return book_contents

def print_report(book, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        for k,v in item.items():
            if k.isalpha():
                print(f"{k}: {v}")

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    # print(get_book_test(book))
    num_words = stats.get_num_words(book)
    # print(f"{num_words} words found in the document")
    char_num_dict = stats.get_char_num(book)
    # print(f"{char_num_dict}")
    sorted_char_count_list = stats.sort_char_count(char_num_dict)

    print_report(book, num_words, sorted_char_count_list)


if __name__ == '__main__':
    main()