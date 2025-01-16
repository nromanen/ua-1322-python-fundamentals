"""
Write a function that calculates the number of characters
included in a given string.
"""

user = input('Enter your word: ')


def counter_letters(word: str) -> dict:
    """This function counts the occurrences of letters in a word."""
    found = {}
    for letter in word:
        if letter.isdigit(): # перевіряємо чи символ є цифрою
            continue
        found.setdefault(letter, 0)  # ініціалізуємо символ та його початкове значення
        found[letter] += 1 # збільшуємо значення на один
    return found


print(counter_letters(user))
