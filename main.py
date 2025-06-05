from stats import word_count, char_count, char_sorter

def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	count = word_count(text)
	chars_dict = char_count(text)
	chars_sorted_list = char_sorter(chars_dict)
	print_report(book_path, count, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, count, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

	 
if __name__ == "__main__":
	main()
