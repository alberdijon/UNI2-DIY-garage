from copyreg import pickle
from BasicMethods import *
from Cabin import *
import pickle

class CabinMethods:
    def add_cabins():

        #Cabin.set_id(Cabin,BasicMethods.askInteger("id"))
        #Cabin.set_type(Cabin,BasicMethods.askString("type"))
        #Cabin.set_pricePerHour(Cabin,BasicMethods.askInteger("pricePerHour"))
        #Cabin.set_availability(Cabin,BasicMethods.askString("availability"))
        new_cabin = Cabin(BasicMethods.askInteger("id"), BasicMethods.askString("type"), BasicMethods.askInteger("pricePerHour"), BasicMethods.askString("availability"))
        #new_cabin.set_id(BasicMethods.askInteger("id")) objetua hutsik sortu eta horrela bete

        with open("Cabins.pkl", "ab") as f:
            pickle.dump(new_cabin, f)
        print("User added")
        new_cabin = 0
        CabinMethods.menu_cabins()

    def view_cabins():
        inp=open('Cabins.pkl', 'rb')
        cabins = []
        cont=1
        iterations =0
        while cont == 1:
                iterations += 1
                try:
                    cabins.append(pickle.load(inp))
                except EOFError:
                    print("Showing "+str(iterations-1)+" cabins -->")
                    cont=0
        for cab in cabins:
            cab.print()
            (str(cab.id)+" "+cab.type+" "+str(cab.pricePerHour)+" "+cab.availability)
        CabinMethods.menu_cabins()
            
            
    def available_cabins():
        inp=open('Cabins.pkl', 'rb')
        cabins = []
        cont=1
        iterations =0
        while cont == 1:
                iterations += 1
                try:
                    cabins.append(pickle.load(inp))
                except EOFError:
                    cont=0
        for cab in cabins:
            if cab.availability== "available":
                print(str(cab.id)+" "+cab.type+" "+str(cab.pricePerHour)+" "+cab.availability)
        CabinMethods.menu_cabins()
                        

        CabinMethods.menu_cabins()
    def condition_cabins():
        inp=open('Cabins.pkl', 'rb')
        cabins = []
        cont=1
        while cont == 1:
            
            try:
                    cabins.append(pickle.load(inp))
            except EOFError:
                    cont=0
        select_cabin=BasicMethods.askInteger("ID")
        for cab in cabins:
            if cab.id == select_cabin:
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
            print("Good Bye!")
        else:
            print("Wrong value, please repeat the process")
            CabinMethods.menu_cabins()