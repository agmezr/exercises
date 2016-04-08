
def count_words(text):
	dic = {}

	for word in text.strip().split(" "):
		word_length = len(word)
		if word_length == 0 or word_length == " ":
			continue
		if word_length in dic:
			dic[word_length].append(word)
		else:
			dic[word_length] = [word]

	return dic


if __name__ == '__main__':
	text = "the brown fox jumps in a pool   "

	print count_words(text)