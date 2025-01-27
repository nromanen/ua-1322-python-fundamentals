#https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python

def reverse(st): 
    words = st.strip().split() 
    reversed_words = words[::-1]
    return " ".join(reversed_words)
