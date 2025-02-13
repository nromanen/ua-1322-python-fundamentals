# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

# II. Find The Distance Between Two Points
import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

# III. No yelling!
def filter_words(sentence):
    words = sentence.strip().split()
    return ' '.join([words[0].capitalize()] + [word.lower() for word in words[1:]])

# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)

# V. Reversing Words in a String
def reverse_words(string):
    return ' '.join(string.strip().split()[::-1])

# VI. Reverse List Order
def reverse_list(lst):
    return lst[::-1]

# VII. Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

# X. Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(b):
    return "Yes" if b else "No"

# XI. Counting sheep
def count_sheeps(sheep):
    return sum(sheep)

# XII. Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail