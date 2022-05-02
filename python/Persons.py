class Person:

    def __init__(self, i, n, s, g, m):
        self.id = i
        self.name = n
        self.surname = s
        self.gmail = g
        self.mobile = m

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

    def print(self):
        print(self.id,self.name, self.surname, self.gmail, self.mobile)
