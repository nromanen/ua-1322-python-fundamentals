class Human():
    '''Human class i guess'''
    def __init__(self, fname):
        self.name = fname

    def welcome(self):
        print(f"Hey there, {self.name}")


class Homosapiens(Human):
    '''Exclusive to homosepians'''
    def __init__(self, fname = "NONE"):
        super().__init__(fname)
        self.species = "Homosapien"
    
    def human_welcome(self):
        print(f"Return to Monke, {self.name}")


if __name__ == "__main__":
    person1 = Homosapiens("Bob")
    person1.welcome()
    person1.human_welcome()

    # if person1.species != "Homosapien":
    #     print ("Ooga Booga")
    # else:
    #     print ("A man of culture.")