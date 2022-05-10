from copyreg import pickle
from BasicMethods import *
from Cabin import *
import pickle

class CabinMethods:
    def add_Cabins():
        
        try:
            with open("Cabins.pkl", "rb") as f:
                cabins = pickle.load(f)
        except EOFError:
            cabins = []
            print("No users in database")

        Cabin.set_id(Cabin,BasicMethods.askInteger("id"))
        Cabin.set_type(Cabin,BasicMethods.askString("type"))
        Cabin.set_pricePerHour(Cabin,BasicMethods.askInteger("pricePerHour"))
        Cabin.set_availability(Cabin,BasicMethods.askString("availability"))
        new_cabin = Cabin(Cabin.id, Cabin.type, Cabin.pricePerHour, Cabin.availability)
        cabins.append(new_cabin)
        with open("Cabins.pkl", "wb") as f:
            pickle.dump(cabins, f)
        print("User added")

    def view_cabins():
        inp=open('Cabins.pkl', 'rb')
        cabins= []
        cont=1
        while cont == 1:
            try:
                cabins.append(pickle.load(inp))
            except EOFError:
                print("end of cabins")
                cont=0
        for cab in cabins:
            print(cab)
            Cabin.print_(cab)
            
    def available_cabins():
        inp=open('Cabins.pkl', 'rb')
        cabins= []
        cont=1
        while cont == 1:
            try:
                cabins.append(pickle.load(inp))
            except EOFError:
                print("end of cabins")
                cont = 0
        for cab in cabins:
            if Cabin.get_availability == "available":
                print(cab)
    

