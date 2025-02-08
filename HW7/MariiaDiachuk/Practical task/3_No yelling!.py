def filter_words(st):
    words = st.split()
    return ' '.join([words[0].capitalize()] + [word.lower() for word in words[1:]])
