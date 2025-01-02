"""
Interchange the values of two variables without using the third variable
"""

variable_1 = "ONE "
variable_2 = "TWO "

print(f"Variables in their initial order: variable_1 is {variable_1}, variable_2 is {variable_2}")

variable_1, variable_2 = variable_2, variable_1

print(f"Variables reversed: variable_1 is {variable_1}, variable_2 is {variable_2}")

