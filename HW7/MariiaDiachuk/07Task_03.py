def count_characters(s):
    char_count = {}
    
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    
    return char_count


input_string = "hello"
result = count_characters(input_string)
print(result)
