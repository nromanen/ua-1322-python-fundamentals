word = input("Enter the word: ")
number = {}
for letter in word:
    if letter not in number: #check each letter and if it was not previously in the set, assign it a value =1 
        number[letter] = 1
    else:
        number[letter] += 1 #if this letter was in the set, count the number
print(number)
