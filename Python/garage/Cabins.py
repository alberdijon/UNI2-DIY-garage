from BasicMethods import *
import pickle


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
       pkl = open("Cabins.pkl","r")
       for line in pkl:
           print(line)
    def available_cabins():
        pkl = open("Cabins.pkl","r")
        for line in pkl:
            line.split(",",3 )
            c1=Cabins(line[0],line[1],line[2],line[3])
            print(line[0],line[1],line[2],line[3])
           
    def change_estatus():
        with open("Cabins.pkl","rb") as f:
            pkl= pickle.load(f)
            allCabins=[]
            for line in pkl:
                allCabins.append(line.split(","))
            id=int(BasicMethods.askInteger("ID"))-1
            estatus=input("What estatus you want apply? 1 for available, 2 for occupied and 3 for repairing ")
            if estatus == "1":
                allCabins[id][3]="available"
            
            if estatus == "2":
                allCabins[id][3]="occupied"
                
                
            if estatus == "3":
                allCabins[id][3]="repairing"
            else :
                print("Wrong value, repeat please")
            

    def cabinsMenu():
        BasicMethods.MenuOptions()
        option=BasicMethods.askInteger("option")
        while option !=0:
            BasicMethods.MenuOptions()
            option=BasicMethods.askInteger("option")
            if option == 1 :
                Cabins.view_cabins()
            if option == 2 :
                Cabins.available_cabins()
            if option == 3 :
                Cabins.change_estatus()
            else:
                print("Wrong value, please repeat the process")

            

                

           
    

