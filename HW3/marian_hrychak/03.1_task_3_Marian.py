"""Interchange the values of two variables without using the third variable."""

first_var = 10
second_var = 20

print(f"Before first_var = {first_var}, second_var = {second_var}")

first_var, second_var = second_var, first_var

print(f"After first_var = {first_var}, second_var = {second_var}")
