from Cabins import *

class BasicMethods:

    def askInteger(name):
        a=int(input("Enter a value for "+ name+": "))
        return a 
    def askString(name):
        a=input("Enter a value for "+ name+": ")
        return a
    def askBoolean(name):
        a=int(input("Enter a value for "+ name+" 1 for yes, 2 for no: "))
        if a==1:
            available=True
            return available
        if a==0:
            available=False
            return available
        else:
            print("Wrong value, please repeat the process")
    
    def Cabins_menu():
        print("1- Show all cabins")
        print("2-Show available cabins")
        print("3-Change the estatus of the cabins")
        print("0-Exit the program")