"""
Create a class Human, everyone has a name, create a method in the
class that displays a welcome message to each person. Create a class method
in the class that returns information that it is a species of "Homosapiens".
And in the class create a static method that returns an arbitrary message.
"""

class Human:

    name = None

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, {self.name}!"

    @classmethod
    def cls_method(cls, name):
        return f"{name} is a 'Homosapiens'."

    @staticmethod
    def st_method():
        return f"This is an arbitrary message."


person_1 = Human("John")

print(person_1.welcome_message())
print(Human.cls_method(person_1.name))
print(person_1.st_method())
