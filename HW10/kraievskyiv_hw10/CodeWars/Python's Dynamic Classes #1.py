import re

def class_name_changer(cls, new_name):
    if not re.match(r"^[A-Z][a-zA-Z0-9]*$", new_name):
        raise ValueError
    else:
        cls.__name__ = new_name
        return cls.__name__