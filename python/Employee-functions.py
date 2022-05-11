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

        print(employee.id)
    employee_menu()


def hire():

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

    # Overwrites any existing file.
        with open('employees.pkl', 'ab') as f:
            pickle.dump(employee, f)
        print("Added succesfully")
        del employee
        ans = int(input("Do you want to add a new employee? (1/0)"))
    employee_menu()


def fire():
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
            with open("employees.pkl", "wb") as f:
                pickle.dump(employees, f)
            print("employee edited")
            employee_menu()
    print("no employee found")
    employee_menu()


employee_menu()