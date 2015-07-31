
def word_count(filepath):
	"""
	Counts the number of occurences of each unique word in a file.
	Input
	-----
	filepath: str
		Path to a text file.
	Output
	-----
	Prints words and their frequencies.

	"""

	raven_text = open('raven.txt')
	raven_dict = {}
	for line in raven_text:
		list_words = line.strip().split()
		for word in list_words:
			word = word.strip(".,;:\'\"-?!").lower()
			try:
				raven_dict[word] += 1
			except KeyError:
				raven_dict[word] = 1
	raven_text.close()

	word_counter = sorted(raven_dict.items(), key = lambda x: x[1], reverse = True)
	
	f_out = open('word_counts.txt', 'w')		
	for word, number in word_counter:
		f_out.write("{}: {}\n".format(word,number))
	f_out.close()

word_count('raven.txt')