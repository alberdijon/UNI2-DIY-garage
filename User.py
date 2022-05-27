from BasicMethods import BasicMethods
from Person import Person

class User(Person):
    def __init__(self, p):
        super().__init__(self)
        self.pasword = p

    def setPassword(self):
        self.pasword = BasicMethods.askString("the pasword: ")
    
    def getPassword(self):
        return self.pasword   
    
    def print(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Last name: ", self.last_name)
        print("Email: ", self.email)
        print("Phone number: ", self.phone_number)
        print("Password: ", self.pasword)