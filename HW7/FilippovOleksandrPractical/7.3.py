#https://www.codewars.com/kata/587a75dbcaf9670c32000292/train/python

def filter_words(st):
    words_list = st.split()
    words = ' '.join(words_list)
    joined_words  = words.capitalize()
    return joined_words  
    
    