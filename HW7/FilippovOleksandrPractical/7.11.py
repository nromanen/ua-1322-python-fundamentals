# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python

def count_sheeps(sheep):
  return sum(1 for item in sheep if item is True)