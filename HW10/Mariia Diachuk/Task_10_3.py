class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @staticmethod
    def total_employees():
        print(f"Total number of employees: {Employee.employee_count}")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

emp1.display_info()
emp2.display_info()

Employee.total_employees()

print(f"Base classes: {Employee.__bases__}")
print(f"Class dictionary: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
