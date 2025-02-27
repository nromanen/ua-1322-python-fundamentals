def class_name_changer(cls, new_name):
    # Check if new_name is valid: starts with uppercase and contains only alphanumeric characters
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise ValueError("The new name must start with an uppercase letter and contain only alphanumeric characters.")
