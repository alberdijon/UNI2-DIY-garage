import pickle

from Person import *


def employee_menu():
    ans = True
    while ans:
        print("""
        Menu > Employees
        1.View Employees
        2.Hire
        3.Fire
        4.Edit
        0.Exit
        """)
        ans = input("What would you like to do?")

        if ans == "1":
            viewemployees()
        elif ans == "2":
            hire()
        elif ans == "3":
            fire()
        elif ans == "4":
            edit_employees()
        elif ans == "0":
            print("\n Goodbye")
            exit()
        else:
            print("\n Not Valid Choice Try again")
            employee_menu()


def viewemployees():
    inp = open('employees.pkl', 'rb')
    try:
        employees = pickle.load(inp)

    except EOFError:
        print('end of employees')

        employees = []
    for employee in employees:
        print(employee.id, employee.name, employee.surname, employee.gmail, employee.mobile, employee.job,
              employee.salary)
    employee_menu()


def hire():

    try:
        with open('employees.pkl', 'rb') as f:
            employees = pickle.load(f)
    except EOFError:
        employees = []
    ans = 1
    while ans == 1:
        id = input("Add new employee id: ")
        name = input("Add new employee name: ")
        surname = input("Add new employee surname: ")
        gmail = input("Add new employee gmail: ")
        mobile = input("Add new employee phone number: ")
        job = input("Add new employee job: ")
        salary = input("Add new employee salary: ")
        employee = Employee(id, name, surname, gmail, mobile, job, salary)

            # sample usage
        employees.append(employee)

        ans = int(input("Do you want to add a new employee? (1/0)"))
        del employee
    # Overwrites any existing file.
        with open('employees.pkl', 'wb') as f:
            pickle.dump(employees, f)
        print("Added succesfully")
    employee_menu()


def fire():
    with open("employees.pkl", "rb") as f:
        employees = pickle.load(f)
    employee_to_delete = input("Enter the id of the employee you want to delete: ")

    for employee in employees:
        if employee.id == employee_to_delete:
            employees.remove(employee)

    with open("employees.pkl", "wb") as f:
        pickle.dump(employees, f)
    print("Deleted succesfully")
    employee_menu()


def edit_employees():
    try:
        with open("employees.pkl", "rb") as f:
            employees = pickle.load(f)

    except EOFError:
        employees = []
    employee_to_edit = input("Enter the id of the employee you want to edit: ")
    for employee in employees:
        if employee.id == employee_to_edit:
            id = input("Add new employee id: ")
            name = input("Add new employee name: ")
            surname = input("Add new employee surname: ")
            gmail = input("Add new employee gmail: ")
            mobile = input("Add new employee phone number: ")
            job = input("Add new employee job: ")
            salary = input("Add new employee salary: ")
            employee.id = id
            employee.name = name
            employee.surname = surname
            employee.gmail = gmail
            employee.mobile = mobile
            employee.job = job
            employee.salary = salary
            with open("employees.pkl", "rb") as f:
                pickle.dump(employees, f)
            print("employee edited")
            employee_menu()
    print("no employee found")
    employee_menu()


class Employee(Person):

    def __init__(self, ei, en, es, eg, em, j, s):
        self.id = ei
        self.name = en
        self.surname = es
        self.gmail = eg
        self.mobile = em
        self.job = j
        self.salary = s

    def setid(self):
        id = input("Enter the value of the id")

    def getid(self):
        return self.id

    def setname(self):
        name = input("Enter the value of the name")

    def getname(self):
        return self.name

    def setsurname(self):
        surname = input("Enter the value of the surname")

    def getsurname(self):
        return self.surname

    def setmobile(self):
        mobile = input("Enter the value of the mobile")

    def getmobile(self):
        return self.mobile

    def setgmail(self):
        gmail = input("Enter the value of the gmail")

    def getgmail(self):
        return self.gmail

    def setjob(self):
        job = input("Enter the value of the job")

    def getjob(self):
        return self.job

    def setsalary(self):
        salary = input("Enter the value of the salary")

    def getgmail(self):
        return self.salary

    def print(self):
        print(self.id, self.name, self.surname, self.gmail, self.mobile, self.job, self.salary)


employee_menu()