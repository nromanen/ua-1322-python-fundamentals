class Employee():
    '''Keeping track of employees and salaries!'''
    employee_num = 0
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
        Employee.employee_num += 1


    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    
    # (* args, ** kwargs) So we can print employee count with both person1.employee_count() and Employee.employee_count()
    # without getting errors, please let me know if there is a better way to do this.
    def employee_count(* args, ** kwargs):
        print(f"Total number of employees: {Employee.employee_num}")

    # needed to reduce employee count if we delete someone.
    # def __del__(self):
    #     Employee.employee_num -= 1
    #     print(f"{self.name} has been removed from the count!")
    


if __name__ == "__main__":
    person1 = Employee("Bob", 50)
    print("-"*30)
    Employee.employee_count()
    person1.employee_info()
    print("-"*30)
    print(Employee.__base__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)