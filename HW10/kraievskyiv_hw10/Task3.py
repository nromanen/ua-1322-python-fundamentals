class Employee:
    """
    Class stores total number of employees,
    their names and salary.
    """
    #Counter that calculates the total number of employees
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def show_info(self):
        """Display info about employee"""
        print(f"Employee: {self.name}\nSalary: ${self.salary}")    
    
    @classmethod
    def total_employees(cls):
        """Display total employees count """
        print(f"Total number of employees is {cls.employee_count}")


emp1 = Employee("Arnold", "2500")
emp2 = Employee("Adam", "3000")

Employee.total_employees()
emp1.show_info()
emp2.show_info()

#Display information about the class
print(f"Base classes: {Employee.__base__}")
print(f"Namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")