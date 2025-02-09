class Human:
    name = None

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls):
        return "Your species is 'Homosapiens'."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message"


# Example
person1 = Human("Bob")
person1.welcome_message()  # Instance
print(Human.species())  # Class
print(Human.arbitrary_message())  # Static
