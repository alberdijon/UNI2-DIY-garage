from copyreg import pickle
from BasicMethods import *
from Cabin import *
from pickle import *

class CabinMethods:
    def add_Cabins():
        
        try:
            with open("Cabins.pickle", "rb") as f:
                cabins = pickle.load(f)
        except EOFError:
            cabins = []
            print("No users in database")
    valid = True
    id(BasicMethods.askInteger("id"))
    type(BasicMethods.askString("type"))
    pricePerHour(BasicMethods.askInteger("pricePerHour"))
    for Cabin in cabins:
        if Cabin.id == id:
            print("Id already in use")
            print("Returning to main menu")
            valid = False
    if valid:
        password = input("Enter password: ")
        phone_number = input("Enter phone number: ")
        new_cabin = Cabin(id, type, pricePerHour, availability, phone_number)
        cabins.append(new_cabin)
        with open("users.pickle", "wb") as f:
            pickle.dump(users, f)
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
        for Cabin in cabins:
            print(Cabin.id())

