# Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}
def num_char(string):
    result = {}
    for i in string:
        if i not in result:
            x = string.count(i)
            result[i] = x
    return result


word = input('Enter a string: ')
print(num_char(word))
