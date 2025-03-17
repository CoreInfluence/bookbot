def get_num_words(bookname):
    book_path = f"books/{bookname}.txt"
    # print(book_path)
    with open(book_path,"r") as book:
        book_contents = book.read()
        book_contents_list = book_contents.split()
        return len(book_contents_list)
        # print(book_contents_list)