with open("Zen.txt", "r") as file:
    file = file.read()
    content = file.replace("\n", " ")
    print(content)

    word_better = "better"  # присвоюємо слова і рахуємо їх кількість
    word_is = "is"
    word_never = "never"

    count_better = content.count(word_better)

    count_is = content.count(word_is)

    count_never = content.count(word_never)
    print(
        f" Слово {word_better} повторюється {count_better} раз(и).\n Слово {word_is} повторюється {count_is} раз(и).\n Слово {word_never} повторюється {count_never} раз(и)."
    )

content_upper = content.upper()  # перетворюємо текст на верхній регістр
print(content_upper)
new_content=content_upper.replace("I","&")  # замінюємо букву І на ?
print(new_content)