# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    if name.find('R') == 0 or name.find('r') == 0:
        result = name + ' plays banjo'
    else:
        result = name + ' does not play banjo'
    return result
