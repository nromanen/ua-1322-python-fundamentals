#Task 1
class Poligon:
    """create a base class Poligon"""
    def __init__(self, a,b):
        self.a = a
        self.b = b

class Rectangle(Poligon):
    """create a child class Rectangle"""
    def square(self):
        return self.a * self.b

print(Rectangle(3,5).square())
print(Rectangle(6.5,5.1).square())



#Task 2
class Human:
    def __init__(self, name):
        self.name = name
        print(f"Hello {self.name}!")
    def species(self):
        return f"{self.name} is Homosapiens"
    @staticmethod
    def static():
        print("I'm Human class static method!")

human1 = Human("Homer")
print(human1.species())
Human.static()



#Task 3
class Employee(object):
    """Employee class"""
    employees = list()

    def __new__(self, *args, **kwargs):
        self.obj =  None
        if not self.obj:
            self.obj = object.__new__(self)
        return self.obj

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.employees.append({'Name': self.name, 'Salary': self.salary})

    @classmethod
    def get_count(cls):
        return len(cls.employees)

    def info(self):
        print(f"Total employees: {Employee.get_count()}")
        for employee in self.employees:
            print(f"Name: {employee['Name']} | Salary: {employee['Salary']}")


Employee1 = Employee("Dmytro","40000")
Employee2 = Employee("Roza","20000")
Employee3 = Employee("Ivan", "30000")
Employee3.info()
print(Employee.__dict__)
print(Employee.__base__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)