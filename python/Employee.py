

from Person import *





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


