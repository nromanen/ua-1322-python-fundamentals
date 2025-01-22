# Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.


class Human:
    def __init__(self, name):
        self.person_name = name

    def welcome_message(self):
        print(f'Hello, {self.person_name}!')

    @classmethod
    def classmethod(cls):
        return 'Homosapiens'

    @staticmethod
    def staticmethod():
        return 'Good by!'


man = Human('Ihor')
man.welcome_message()
print(man.classmethod())
print(man.staticmethod())
