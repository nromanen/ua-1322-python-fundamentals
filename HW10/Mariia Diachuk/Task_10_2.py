class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name}! Welcome!")

    @classmethod
    def species_info(cls):
        return "This species is Homo sapiens"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message!"



person = Human("Alice")

person.welcome()

print(Human.species_info())

print(Human.arbitrary_message())
