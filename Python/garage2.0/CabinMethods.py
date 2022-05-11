from copyreg import pickle
from BasicMethods import *
from Cabin import *
import pickle

class CabinMethods:
    def add_cabins():

        Cabin.set_id(Cabin,BasicMethods.askInteger("id"))
        Cabin.set_type(Cabin,BasicMethods.askString("type"))
        Cabin.set_pricePerHour(Cabin,BasicMethods.askInteger("pricePerHour"))
        Cabin.set_availability(Cabin,BasicMethods.askString("availability"))
        new_cabin = Cabin(Cabin.id, Cabin.type, Cabin.pricePerHour, Cabin.availability)
        with open("Cabins.pkl", "ab") as f:
            pickle.dump(new_cabin, f)
        print("User added")
        del new_cabin
        CabinMethods.menu_cabins()

    def view_cabins():
        inp=open('Cabins.pkl', 'rb')
        cabins= []
        cont=1
        while cont == 1:
            try:
                cabins.append(pickle.load(inp))
                for cab in cabins:
                    print(str(cab.id)+" "+cab.type+" "+str(cab.pricePerHour)+" "+cab.availability)
                    del cab
            except EOFError:
                print("end of cabins")
                cont=0
        CabinMethods.menu_cabins()
            
            
    def available_cabins():
        inp=open('Cabins.pkl', 'rb')
        cabins = []
        cont=1
        while cont == 1:
            try:
                cabins.append(pickle.load(inp))
                for cab in cabins:
                    if cab.availability == "available":
                        print(str(cab.id)+" "+cab.type+" "+str(cab.pricePerHour)+" "+cab.availability)
                        
            except EOFError:
                print("end of cabins")
                cont = 0
        CabinMethods.menu_cabins()
    def condition_cabins():
        inp=open('Cabins.pkl', 'rb')
        cabins = []
        cabins.append(pickle.load(inp))
        select_cabin=BasicMethods.askInteger("ID")
        for cab in cabins:
            if cab.id is select_cabin:
                print(str(cab.id)+" "+cab.type+" "+str(cab.pricePerHour)+" "+cab.availability)
                a = int(input("1 for available 2 for occupied 3 for repairing --> "))
                if a == 1:
                    cab.availability = "available"
                    print(str(cab.id)+" "+cab.type+" "+str(cab.pricePerHour)+" "+cab.availability)
                elif a == 2:
                    cab.availability = "occupied"
                    print(str(cab.id)+" "+cab.type+" "+str(cab.pricePerHour)+" "+cab.availability)
                elif a == 3:
                    cab.availability = "repairing"
                    print(str(cab.id)+" "+cab.type+" "+str(cab.pricePerHour)+" "+cab.availability)
                else:
                    print("Wrong number try again")
            BasicMethods.saveObjects('Cabins.pkl', cabins, cab)
            CabinMethods.menu_cabins()

    

    def menu_cabins():
        BasicMethods.menu()
        a=BasicMethods.askInteger("Menu option")
        if a == 1:
            CabinMethods.add_cabins()
        if a == 2:
            CabinMethods.view_cabins()
        if a == 3:
            CabinMethods.available_cabins()
        if a == 4:
            CabinMethods.condition_cabins()
        if a == 5:
            print("")
        else:
            print("Wrong value, please repeat the process")