import pickle
from Cabins import *
from BasicMethods import *

class Methods_cabins:
    def create_cabins():
        try:
            with open("Cabins.pickle", "rb") as f:
                cabins = pickle.load(f)

        except EOFError:
            cabins = []
            print("No cabins in database")

        valid = True
        id = BasicMethods.askInteger("ID")
        pricePerHour = BasicMethods.askInteger("Price Per Hour")
        type = BasicMethods.askString("Type")
        availability = BasicMethods.askString("Availability")
        for Cabin in cabins:
            if Cabin.id == id:
                print("ID already in use")
                print("Returning to main menu")
        valid = False
        if valid:
            new_cabin = Cabin(id, pricePerHour, type, availability)
            cabins.append(new_cabin)
        with open("Cabins.pickle", "wb") as f:
            pickle.dump(cabins, f)
            print("Cabin added")
            print("",end="\n")
        BasicMethods.MenuOptions()
    def view_cabins():
        inp= open("Cabins.pickle", "rb")
        cabins= []
        cont=1
        while cont == 1:
            try:
                cabins.append(pickle.load(inp))

            except EOFError:
                print("No more cabins in database \n")
                cont=0

        #for cab in cabins:
        print(cabins)  

    def available_cabins():
        with open("Cabins.pickle", "rb") as f:
            try:
                cabins = pickle.load(f)

            except EOFError:
                print("No cabins in database")
                cabins = []
        for Cabin in cabins:
            if Cabin.availability == "available":
                print(Cabin(S))


           
    def change_estatus():
        with open("Cabins.pickle","rb") as f:
            pickle= pickle.load(f)
            allCabins=[]
            for line in pickle:
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
                Cabin.view_cabins()
            if option == 2 :
                Cabin.available_cabins()
            if option == 3 :
                Cabin.change_estatus()
            else:
                print("Wrong value, please repeat the process")
