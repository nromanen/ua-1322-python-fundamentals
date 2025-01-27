"""
Create a list that contains elements of integer type, then use
the loop to change the type of these elements to a floating type.
"""

from random import randint

int_list = []
while len(int_list) != 10:
    int_list.append(randint(1, 100))

float_list = [float(i) for i in int_list]

print(int_list)
print(float_list)
