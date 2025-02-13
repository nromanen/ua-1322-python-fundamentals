def count_characters(s):
    """
    Calculate the number of occurrences of each character in a string.
    
    Parameters:
    s (str): The input string
    
    Returns:
    dict: A dictionary with characters as keys and their counts as values
    """
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

print(count_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}