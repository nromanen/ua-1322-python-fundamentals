class Human():
    """
    Class displays a welcome message to each person,
    information that humans are "Homosapiens" and
    an arbitrary message.
    """
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name
        print(f"Welcome {self.name}!")
    
    @classmethod
    def species_info(cls):
        """Display info about humans species"""
        return f"Humans are {cls.species}"
    
    @staticmethod
    def useless_info():
        """Display arbitrary message"""
        return "This is arbitrary message"

obj = Human('Andrew')

print(obj.species_info())
print(obj.useless_info())