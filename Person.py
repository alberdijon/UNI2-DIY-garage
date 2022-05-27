from re import L
from this import d
from tkinter import N
from BasicMethods import BasicMethods

class Person:
    def __init__(self, d, n, l, e, pn):
        self.id = d
        self.name = n
        self.last_name = l
        self.email = e
        self.phone_number = pn

    def setIdWP(self,id):
        self.id
    def setId(self):
        self.id = BasicMethods.askInteger("the id: ")

    def getId(self):
        return self.id

    def setName(self):
        self.name = BasicMethods.askString("the name: ")

    def getName(self):
        return self.name
    
    def setLastName(self):
        self.last_name = BasicMethods.askString("the last name: ")

    def getLastName(self):
        return self.last_name
    
    def setEmail(self):
        self.email = BasicMethods.askString("the email: ")
    
    def getEmail(self):
        return self.email

    def setPhoneNumber(self):
        self.phone_number = BasicMethods.askInteger("the phone number: ")
    
    def getPhoneNumber(self):
        return self.phone_number
    
    def print(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Last name: ", self.last_name)
        print("Email: ", self.email)
        print("Phone number: ", self.phone_number)