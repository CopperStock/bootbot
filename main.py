from stats import word_count, char_count

def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	count = word_count(text)
	chars_dict = char_count(text)
	print(f"{count} words found in the document")
	print(chars_dict)
		

def get_book_text(path):
	with open(path) as f:
		return f.read()


	 
if __name__ == "__main__":
	main()
