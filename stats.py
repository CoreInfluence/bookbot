def get_num_words(book_path):
    # book_path = f"books/{bookname}.txt"
    # print(book_path)
    with open(book_path,"r") as book:
        book_contents = book.read()
        book_contents_list = book_contents.split()
        return len(book_contents_list)

def get_char_num(book_path):
    # book_path = f"books/{bookname}.txt"
    # print(book_path)
    num_char_dict = {}
    with open(book_path,"r") as book:
        book_contents = book.read()
        book_contents_list = book_contents.split()
        for word in book_contents_list:
            for char in word:
                key = char.lower()
                if key in num_char_dict:
                    num_char_dict[f'{key}'] += 1
                else:
                    num_char_dict[f'{key}'] = 1

        return num_char_dict
def sort_char_count(num_char_dict):
    sorted_dict_list = []
    for key, value in dict(sorted(num_char_dict.items(), key=lambda item: item[1],reverse=True)).items():
        key_dict = {key: value}
        sorted_dict_list.append(dict(key_dict))

    return sorted_dict_list
