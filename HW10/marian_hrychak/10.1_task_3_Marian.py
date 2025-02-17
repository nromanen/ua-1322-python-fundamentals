"""
Create an employee class. Each employee has characteristics such as name
and salary. The class should have a counter that calculates the total
number of employees, as well as a method that prints the total number of
employees and a method that displays information about each employee in
particular, namely the name and salary.
In addition to creating a class, display information about the base classes
from which the employee class is inherited (__base__), the class namespace
(__dict__), the class name (__name__), the module name in which the class is
defined (__module__), the documentation bar ( __doc__).
"""

class Employee:

    name = None
    salary = 0
    total_headcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_headcount += 1

    @classmethod
    def counter(cls):
        """This method prints the total number of employees."""
        print(f"Total number of employees: {cls.total_headcount}.")

    def personal_info(self):
        """This method prints the personal information about each employee."""
        print(f"Name: {self.name}, Salary: {self.salary}.")


worker_1 = Employee("John", 20000)
worker_2 = Employee("Donald", 25000)
worker_3 = Employee("Ronald", 17500)

worker_1.personal_info()
worker_2.personal_info()
worker_3.personal_info()
Employee.counter()

print(f"Base classes: {Employee.__bases__}",
      f"Class namespace: {Employee.__dict__}",
      f"Class name: {Employee.__name__}",
      f"Module name: {Employee.__module__}",
      f"Documentation bar: {Employee.__doc__}",
      sep='\n')
