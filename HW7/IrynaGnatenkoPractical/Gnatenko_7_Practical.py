# pylint: skip-file

""" -------------------- 1 --------------------
https://www.codewars.com/kata/55225023e1be1ec8bc000390
Jenny has written a function that returns a greeting for a user.
However, she's in love with Johnny, and would like to greet him slightly different. """

def greet(name):
    if name != "Johnny":
        return f"Hello, {name}!".format(name=name)
    else:
        return "Hello, my love!"


""" -------------------- 2 --------------------
https://www.codewars.com/kata/simple-find-the-distance-between-two-points 
Given two ordered pairs calculate the distance between them. 
Round to two decimal places. This should be easy to do in 0(1) timing. """

import math

def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    d = round(d,2)
    return d


""" -------------------- 3 --------------------
https://www.codewars.com/kata/no-yelling
Write a function taking in a string like "WOW this is REALLY          amazing"
and returning "Wow this is really amazing."
String should be capitalized and properly spaced. Using re and string is not allowed. """

def filter_words(st):
    return " ".join(st.casefold().split()).capitalize()


""" -------------------- 4 --------------------
https://www.codewars.com/kata/convert-a-number-to-a-string
We need a function that can transform a number (integer) into a string. """

def number_to_string(num):
    return str(num)


""" -------------------- 5 --------------------
https://www.codewars.com/kata/reversing-words-in-a-string
You need to write a function that reverses the words in a given string. 
Words are always separated by a single space.
As the input may have trailing spaces, you will also need to ignore unnecessary whitespace.
Example (Input --> Output)
"Hello World" --> "World Hello"
"Hi There." --> "There. Hi" """

def reverse(st):
    return " ".join(reversed(st.split()))


""" -------------------- 6 --------------------
https://www.codewars.com/kata/reverse-list-order
In this kata you will create a function that takes in a list 
and returns a list with the reverse order.
Examples (Input -> Output)
* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9] """

def reverse_list(l):
    return l[::-1]


""" -------------------- 7 --------------------
https://www.codewars.com/kata/multiples-of-3-or-5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once. """

def solution(number):
    i = 1
    number_set = set()
    while i < number:
        if i % 3 == 0:
            number_set.add(i)
        if i % 5 == 0:
            number_set.add(i)
        i += 1
    return sum(number_set)


""" -------------------- 8 --------------------
https://www.codewars.com/kata/will-you-make-it
You were camping with your friends far away from home, but when it's time to go back, 
you realize that your fuel is running out and the nearest pump is 50 miles away! 
You know that on average, your car runs on about 25 miles per gallon. 
There are 2 gallons left.
Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not. """

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False


""" -------------------- 9 --------------------
https://www.codewars.com/kata/are-you-playing-banjo
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings. """

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


""" -------------------- 10 --------------------
https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false. """

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


""" -------------------- 11 --------------------
https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).

For example,
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

The correct answer would be 17.
Hint: Don't forget to check for bad values like null/undefined """

def count_sheeps(sheep):
    return sheep.count(True)


""" -------------------- 12 --------------------
https://www.codewars.com/kata/is-this-my-tail/train/python
Some new animals have arrived at the zoo. 
The zoo keeper is concerned that perhaps the animals do not have the right tails. 
To help her, you must correct the broken function to make sure that the second argument (tail), 
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be non empty strings, and normal letters. """

def correct_tail(body, tail):
    return body[-1] == tail

