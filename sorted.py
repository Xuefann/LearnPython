# -*- coding: utf-8 -*-
"""

	You are given a text, which contains different english letters and punctuation symbols. You should 
find the most frequent letter in the text. The letter returned must be in lower case.While checking for the
most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do
not count punctuation symbols, digits and whitespaces, only letters.If you have two or more letters with the
same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains
"o", "n", "e" only once for each, thus we choose "e".
	Input: A text for analysis as a string.
	Output: The most frequent letter in lower case as a string.
	Precondition:
	A text contains only ASCII symbols.
	0 < len(text) ≤ 105

"""



def checkio(text):
	#filter out not-alphebet char
	if text.isalpha(): text = text.lower()
	else: text = ''.join([x.lower() for x in text if x.isalpha()])
	#print(text)

	from collections import Counter
	str_count = Counter(text)
	#print(str_count)
	#sorted with two parameters,the first parameter is the count of evey char,the second is alphabet
	str_sorted = sorted(Counter(text).items(),key = lambda k:(k[1],k[0]))
	#print(str_sorted)
	#get the most wanted chars
	most_wanted_letters = [item for item in str_sorted if item[1] == str_sorted[len(str_sorted)-1][1]]
	return most_wanted_letters[0][0]

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio("Hello World!") == "l", "Hello test"
	assert checkio("One") == "e", "All letter only once."
	assert checkio("Oops!") == "o", "Don't forget about lower case."
	assert checkio("AAaooo!!!!") == "a", "Only letters."
	assert checkio("abe") == "a", "The First."
	print("Start the long test")
	assert checkio("a" * 9000 + "b"*1000) == "a","long."
	print("The local tests are done.")
