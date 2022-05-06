from re import S
import BasicMethods



class Cabin:
    
    def __init__(self,id,pricePerHour,type,availability):
        self.id = id
        self.pricePerHour = pricePerHour
        self.type = type
        self.availability = availability
    
    def set_id(self,id):
        self.id = BasicMethods.askInteger("ID")
    def set_pricePerHour(self,pricePerHour):
        self.pricePerHour = BasicMethods.askInteger("PricePerHour")
    def set_type(self,type):
        self.type = BasicMethods.askString("Type")
    def set_availability(self,availability):
        self.availability = BasicMethods.askString("Availability")
    def get_id(self):
        print(self.id)
    def get_pricePerHour(self):
        print(self.pricePerHour)
    def get_type(self):
        print(self.type)
    def get_availability(self):
        print(self.availability)
    def print_(self):
        print(self.id + " " + self.pricePerHour + " " + self.type + " " + self.availability)


            

                

           
    

