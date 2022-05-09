from BasicMethods import *

class Cabin:

    def __init__(self, id, type, pricePerHour, availability):
        self.id = Cabin.id()
        self.type = Cabin.type()
        self.pricePerHour = Cabin.pricePerHour()
        self.availability = Cabin.availability()
    
    def id(self):
        return self.id
    def id(self,a):
        self.id = a
    def type(self):
        return self.type
    def type(self,a):
        self.type = a
    def pricePerHour(self):
        return self.pricePerHour
    def pricePerHour(self,a):
        self.pricePerHour = a
    def availability(self):
        return self.availability
    def availability(self,a):
        self.availability = a


    def print_(self):
        print(self.id + " " + self.pricePerHour + " " + self.type + " " + self.availability)
    
