class Employee:
    total_employees = 0
    name = None
    salary = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def display_employee_info(self):
        print(f"Employee's name: {self.name}, Employee's salary: {self.salary}")


# example
emp1 = Employee("Olivia", 35000)
emp2 = Employee("Jenna", 24000)
emp3 = Employee("Jack", 44000)


emp1.display_employee_info()  # information about each employee
emp2.display_employee_info()
emp3.display_employee_info()


Employee.display_total_employees()


print("\nДеталі класу:")
print(f"Базові класи: {Employee.__base__}")
print(f"Простір імен класу: {Employee.__dict__}")
print(f"Ім'я класу: {Employee.__name__}")
print(f"Ім'я модуля: {Employee.__module__}")
print(f"Документація: {Employee.__doc__}")
