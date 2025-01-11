#Function that calculated characters in string and returns dict

def count_char(txt: str) -> dict:
    result = {}
    for char in txt:
        if result.get(char) == None:
            result[char] = 1
        else:
            result[char] += 1
    return result

print(count_char("hello"))

