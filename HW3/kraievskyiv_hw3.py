#Task 1
line = """
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
"""

#Display the text in uppercase
print(line.upper())

#Find the number of occurrences of the words 
#"better", "never" and "is" in the given line
better_occ = line.count("better")
never_occ = line.count("never")
is_occ = line.count("is")

#Print the number of occurrences of each word
print(f'The word "better" appears {better_occ} times.')
print(f'The word "never" appears {never_occ} times.')
print(f'The word "is" appears {is_occ} times.')

#Replace all occurances of "i" with "&"
print(line.replace('i', '&'))


#Task 2
#Specify a four-digit natural number
number = int(input("Enter a four-digit natural number: "))

#Check if the number is a four-digit number
if not len(str(number)) == 4:
  print("Invalid number.")
else:
  print(f'You entered the number {number}.')
  
  #Find and print product of the digits of the entered number
  product = 1
  for digit in str(number):
   product *= int(digit)
  print(f'The product of the digits is {product}.')

  #Write the number in reverse order
  reversed_order = int(str(number)[::-1])
  print(f"In reverse order the number is {reversed_order}")

  #Write the number in asceding order
  ascending_order = sorted(str(number))
  #Turn the list into an integer
  ascending_order = int(''.join(ascending_order))
  print(f"In ascending order the number is {ascending_order}")

#Task 3
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
#Print the values of a and b before interchanging
print(f'Before interchanging, a = {a} and b = {b}')
#Interchange the values of a and b and print new values
a, b = b, a
print(f'After interchanging, a = {a} and b = {b}')