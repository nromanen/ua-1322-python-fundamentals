import re
def class_name_changer(cls, new_name):
    if not re.search(r"^[A-Z][0-9A-Za-z]*$", new_name): raise ValueError
    cls.__name__ = new_name