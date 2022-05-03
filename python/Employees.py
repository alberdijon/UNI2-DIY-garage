import pickle

from Person import *


def viewemployees():
    inp = open('employees.pkl', 'rb')
    employees = []
    cont = 1

    while cont == 1:
        try:
            employees.append(pickle.load(inp))

        except EOFError:
            print('end of employees')
            cont = 0

    for emp in employees:
        print(emp)


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
        emple = Employees(id, name, surname, gmail, mobile, job, salary)

        # sample usage

        ans = int(input("Do you want to add a new student? (1/0)"))
    with open('employees.pkl', 'a') as outp:  # Overwrites any existing file.
        outp.write(f"{emple.id} {emple.name} {emple.surname} {emple.gmail} {emple.mobile} {emple.job} {emple.salary}\n")
    del emple


def fire():
    inp = open('employees.pkl', 'r')
    lines = inp.readlines()
    inp.close()

    n = input('enter the number of the row you want delete')

    del lines[n]

    new_inp = open('employees.pkl', 'w+')

    for line in lines:
        new_inp.write(line)

    new_inp.close()


class Employees(Person):

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






