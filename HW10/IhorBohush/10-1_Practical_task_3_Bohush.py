# Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)


class Employee:
    """This is a class named Employee, that creates objects with name and salary of
    employees. Also, there is a counter that calculates total number of employees"""

    __counter = 0

    def __init__(self, name, salary):
        Employee.__counter += 1
        self.name = name
        self.salary = salary
        self.number_of_employees()
        self.inform_employee()

    def __del__(self):
        Employee.__counter -= 1

    def number_of_employees(self):
        print(self.__counter)

    def inform_employee(self):
        print(self)

    def __str__(self):
        return 'Employee: {}, salary: {}'.format(self.name, self.salary)


Ihor = Employee('Ihor', 1000)
Bohush = Employee('Bohush', 2000)
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
