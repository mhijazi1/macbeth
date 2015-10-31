import operator

#open macbeth.txt, we assume this is in the same directory as macbeth.py
macbeth = open("macbeth.txt")
#initalize a dictionary of words
words = {}


for line in macbeth:
	#remove all punctuation in a line
	out = "".join(c for c in line if c not in (',', '.', '?', ':', ';', '!'))
	line = out	
	for word in line.split():
		#if the lenght of a word is atleast 4 characters
		if(len(word) > 4):
			#set all words to lowercase (this is to make sure we don't counte Macbeth and MACBETH as different words)
			word = word.lower()
			#if the word exists in our dictionary iterate, otherwise initialize it with a value of 1
			words[word] = words.get(word, 0) + 1
#sort all words by their value
sorted_words = sorted(words.items(), key = operator.itemgetter(1))
#sor by decending order
sorted_words = list(reversed(sorted_words))

second_word = sorted_words[1]
print("The second most common word greater than 4 characters in Macbet is \'%s\', occurring a total of %s times" % (second_word[0], second_word[1]))