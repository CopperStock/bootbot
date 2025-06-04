
def word_count(text):
	words = text.split()
	count = len(words)
	return count

def char_count(text):
	chars = {}
	for c in text:
		lowered = c.lower()
		if lowered in chars:
			chars[lowered] += 1
		else:
			chars[lowered] = 1
	return chars
