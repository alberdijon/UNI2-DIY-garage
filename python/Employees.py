import Persons

class Employees(Persons):

    def __init__(self, ei, en, es, eg, em, j, w, s ):

        super.__init__(ei,en, es, eg, em)

        self.job = j
        self.working = w
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
        job = input("Enter the value of the gmail")