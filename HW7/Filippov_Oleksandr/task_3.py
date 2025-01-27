#Task3. Write a function that calculates the number of characters included in a given string.
#input: "hello"
#output: {"h":1, "e":1, "l":2, "o":1}

def char_count(input_string):
    """
    Calculate the number of occurrences of each character in a given string.

    Parameters:
    input_string (str): The string to analyze

    Returns:
    dict: A dictionary with characters as keys and their counts as values
    """
    result = {}
    for char in input_string:
        result[char] = result.get(char, 0) + 1
    return result

# Example usage
input_string = "hello"
output = char_count(input_string)
print(output)  