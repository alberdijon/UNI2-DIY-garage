
import BasicMethods


class Cabins:

    def __init__(self,id,pricePerHour,type,availability):
        self.id = id
        self.pricePerHour = pricePerHour
        self.type = type
        self.availability = availability
    
    def set_id(self,id):
        self.id = BasicMethods.BasicMethods.askInteger("ID")
    def set_pricePerHour(self,pricePerHour):
        self.pricePerHour = BasicMethods.BasicMethods.askInteger("PricePerHour")
    def set_type(self,type):
        self.type = BasicMethods.BasicMethods.askString("Type")
    def set_availability(self,availability):
        self.availability = BasicMethods.BasicMethods.askBoolean("Availability")
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
    def view_cabins():
       txt = open("Cabins.txt")
       for line in txt:
           print(line)
    def available_cabins():
        txt = open("Cabins.txt")
        for line in txt:
            cabineo = (line.split(","))
            a=cabineo[0]
            b=cabineo[1]
            c=cabineo[2]
            d=cabineo[3]
            print(a,b,c,d)
            c1=Cabins(a,b,c,d)
            
            if c1.availability == True:
                    
                    c1.print_


    