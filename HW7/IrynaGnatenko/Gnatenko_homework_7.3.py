"""
Task3. Write a function that calculates the number of characters
included in a given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}
"""


def calc_char(string):
	"""accepts a string and counts how often each character appears in it"""
	char_count = {}
	for i in string:
		x = string.count(i)
		char_count[i] = x
	return char_count


string = input("give me a word: ")
print(calc_char(string))
