"""
You need to write Python's philosophy in the string format:
- find separately the number of occurrences of the words
- "better", "never" and "is" in the given line
- you need to display all text in uppercase (all letters in uppercase)
- replace all occurrences of the symbol “i” with “&”
"""

pythonPhilosophy = str('''Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!''')


"""
find separately the number of occurrences of the words \
"better", "never" and "is" in the given line
"""

# split the multiline string into separate lines:
lines = pythonPhilosophy.splitlines()

# specify which words we want to count:
wordsCounted = ['better','never','is']

# create the variables to contain the line and word we will be working on, \
# assign the first value:
currentLine = str(lines[0])
currentWord = str(wordsCounted[0])

# create a function to count each of the words in the current line:
def word_count():

    for currentWord in wordsCounted:
        wordQuantity: int = currentLine.count(currentWord)
        print(f'{currentWord}:{wordQuantity}')

# print each line and count the words in it, print the result, \
# and add an empty line for better readability:
for currentLine in lines:
    print(f'{currentLine.strip()}')
    word_count()
    print ()

"""
you need to display all text in uppercase (all letters in uppercase)
"""

pythonPhilosophy=pythonPhilosophy.upper()
lines = pythonPhilosophy.splitlines()
currentLine = str(lines[0])

for currentLine in lines:
    print(f'{currentLine.strip()}')

print()

"""
replace all occurrences of the symbol “i” with “&”
"""

pythonPhilosophy=pythonPhilosophy.replace('I','&')

lines = pythonPhilosophy.splitlines()
currentLine = str(lines[0])

for currentLine in lines:
    print(f'{currentLine.strip()}')