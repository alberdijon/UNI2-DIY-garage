import pickle

import Employee
from Employee import *


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
            exit()

        else:
            print("\n Not Valid Choice Try again")
            employee_menu()


def viewemployees():
    f = open('employees.pkl', 'rb')
    employees = []
    cont = 1
    while cont == 1:
        try:

            employees.append(pickle.load(f))

        except EOFError:

            cont = 0
    for employee in employees:
        print(employee.id, employee.name, employee.surname, employee.gmail, employee.mobile, employee.job,
              employee.salary)
    employee_menu()


def hire():
    ans = 'y'
    while ans == 'y':
        id = input("Add new employee id: ")
        name = input("Add new employee name: ")
        surname = input("Add new employee surname: ")
        gmail = input("Add new employee gmail: ")
        mobile = input("Add new employee phone number: ")
        job = input("Add new employee job: ")
        salary = input("Add new employee salary: ")
        employee = Employee(id, name, surname, gmail, mobile, job, salary)

        # Overwrites any existing file.
        with open('employees.pkl', 'ab') as f:
            pickle.dump(employee, f)
        print("Added succesfully")
        del employee
        ans = int(input("Do you want to add a new employee? (y/n)"))
    employee_menu()


def fire():
    viewemployees()
    f = open('employees.pkl', 'rb')
    employees = []
    cont = 1

    while cont == 1:
        try:

            employees.append(pickle.load(f))

        except EOFError:

            cont = 0

    employee_to_delete = input("Enter the id of the employee you want to delete: ")
    for employee in employees:
        e1 = Employee(employee.id, employee.name, employee.surname, employee.gmail, employee.mobile, employee.job,
                      employee.salary)
        try:
            if employee.id == employee_to_delete:

                with open("employees.pkl", "wb") as f:
                    pickle.dump(employee, f)
                    print("Deleted succesfully")

            else:
                with open("employees.pkl", "wb") as f:
                    pickle.dump(e1, f)
        except EOFError:

            print("no employee found")
    employee_menu()


def edit_employees():
    viewemployees()
    f = open('employees.pkl', 'rb')
    employees = []
    cont = 1
    while cont == 1:
        try:

            employees.append(pickle.load(f))

        except EOFError:

            cont = 0

    employee_to_edit = input("Enter the id of the employee you want to edit: ")

    for employee in employees:
        e1 = Employee(employee.id, employee.name, employee.surname, employee.gmail, employee.mobile, employee.job,
                      employee.salary)
        try:

            if employee.id == employee_to_edit:
                id = input("Add new employee id: ")
                name = input("Add new employee name: ")
                surname = input("Add new employee surname: ")
                gmail = input("Add new employee gmail: ")
                mobile = input("Add new employee phone number: ")
                job = input("Add new employee job: ")
                salary = input("Add new employee salary: ")
                e1 = Employee(id, name, surname, gmail, mobile, job, salary)
                with open("employees.pkl", "ab") as f:
                    pickle.dump(e1, f)
                print("employee edited")
            else:
                with open("employees.pkl", "wb") as f:
                    pickle.dump(e1, f)
        except EOFError:

            print("no employee found")
    employee_menu()


employee_menu()
