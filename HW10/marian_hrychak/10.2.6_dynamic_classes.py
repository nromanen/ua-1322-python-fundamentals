"""
Proposed function should allow only names with alphanumeric chars (upper
& lower letters plus ciphers), but starting only with upper case letter.
In other case it should raise an exception.
"""

import re


class MyClass:
    pass


def rename_class(cls, new_name):
    if not isinstance(cls, type):
        raise TypeError("Class must be a type")

    if not re.fullmatch(r'[A-Z][a-zA-Z0-9]*', new_name):
        raise ValueError(
            "Class name must start with an uppercase letter and contain only alphanumeric characters."
        )

    cls.__name__ = new_name


rename_class(MyClass, 'UsefullyClass')
print(MyClass.__name__)
