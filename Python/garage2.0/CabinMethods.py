from copyreg import pickle
from BasicMethods import *
from Cabin import *
import pickle

class CabinMethods:
    def add_cabins():
        new_cabin = Cabin(BasicMethods.askInteger("id"), BasicMethods.askString("type"), BasicMethods.askInteger("pricePerHour"), BasicMethods.askString("availability"))
        with open("Cabins.pkl", "ab") as f:
            pickle.dump(new_cabin, f)
        print("User added")
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
            print(vars(cab))
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
                print(vars(cab))         
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
                print(vars(cab))
                a = int(input("1 for available 2 for occupied 3 for repairing --> "))
                if a == 1:
                    cab.availability = "available"
                    print(vars(cab))
                elif a == 2:
                    cab.availability = "occupied"
                    print(vars(cab))
                elif a == 3:
                    cab.availability = "repairing"
                    print(vars(cab))
                else:
                    print("Wrong number try again")
            BasicMethods.saveObjects('Cabins.pkl', cabins)
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