"""
Employee Management System
Real-time example covering:
variables, datatypes, list, tuple, methods,
class, objects, constructor, inheritance,
interface (abstract class), method overriding,
exception handling, file handling, input/output
"""

# -------------------------------
# 1. VARIABLES & DATA TYPES
# -------------------------------
company_name = "TechVision Pvt Ltd"   # string
total_employees = 0                   # integer
employee_types = ("Full-time", "Intern")  # tuple
departments = ["HR", "IT", "Finance"]     # list

print("Company:", company_name)
print("Departments:", departments)
print("Employee Types:", employee_types)
print("----------------------------------")


# -------------------------------
# 2. INTERFACE (ABSTRACT CLASS)
# -------------------------------
from abc import ABC, abstractmethod

class EmployeeInterface(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_details(self):
        pass


# -------------------------------
# 3. CLASS & OBJECTS + CONSTRUCTOR
# -------------------------------
class Employee(EmployeeInterface):
    def _init_(self, emp_id, name, age, department, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.base_salary = base_salary

    # method overriding from interface
    def calculate_salary(self):
        return self.base_salary

    def get_details(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.department}"


# -------------------------------
# 4. INHERITANCE
# -------------------------------
class FullTimeEmployee(Employee):
    def _init_(self, emp_id, name, age, department, base_salary, bonus):
        super()._init_(emp_id, name, age, department, base_salary)
        self.bonus = bonus

    # overriding method
    def calculate_salary(self):
        return self.base_salary + self.bonus


class InternEmployee(Employee):
    def _init_(self, emp_id, name, age, department, base_salary, stipend):
        super()._init_(emp_id, name, age, department, base_salary)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


# -------------------------------
# 5. INPUT / OUTPUT (Real-time)
# -------------------------------
def take_employee_input():
    try:
        print("\nEnter New Employee Details")
        emp_id = int(input("Employee ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        department = input("Department: ")
        emp_type = input("Type (full/intern): ").lower()

        if emp_type == "full":
            base = int(input("Base Salary: "))
            bonus = int(input("Bonus: "))
            return FullTimeEmployee(emp_id, name, age, department, base, bonus)

        elif emp_type == "intern":
            stipend = int(input("Stipend: "))
            return InternEmployee(emp_id, name, age, department, 0, stipend)

        else:
            raise ValueError("Invalid employee type entered.")

    except Exception as e:
        print("Error:", e)
        return None


# -------------------------------
# 6. FILE HANDLING
# -------------------------------
def save_employee_to_file(employee):
    try:
        with open("employees.txt", "a") as f:
            f.write(employee.get_details() +
                    f", Salary: {employee.calculate_salary()}\n")
        print("Employee saved to file successfully!")

    except Exception as e:
        print("File Error:", e)


def read_employee_file():
    try:
        print("\n----- Employee Records in File -----")
        with open("employees.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No employee file found yet.")


# -------------------------------
# 7. MAIN PROGRAM
# -------------------------------
if _name_ == "_main_":

    employees_list = []  # list

    while True:
        print("\n1. Add Employee")
        print("2. View Saved File Records")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            emp = take_employee_input()
            if emp:
                employees_list.append(emp)
                save_employee_to_file(emp)

        elif choice == "2":
            read_employee_file()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")