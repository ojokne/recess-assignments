# OJOK EMMANUEL NSUBUGA
# REG NUMBER: 21/U/06816/PS
# STUDENT NUMBER: 2100706816


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary > self._salary:
            self._salary = new_salary
            print(f"Salary updated for {self._name}. New salary: {self._salary}")
        else:
            print("Invalid salary increment.")

# Create an instance of the Employee class
employee = Employee("John Doe", 850000)

print(f"Employee Name: {employee.get_name()}")
print(f"Employee Salary: {employee.get_salary()}")

# Increase the salary
employee.set_salary(1000000)

print(f"Updated Employee Salary: {employee.get_salary()}")
