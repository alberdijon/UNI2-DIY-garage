from copyreg import pickle
import pickle

class BasicMethods:
    def askInteger(name):
        a =int(input("Enter a value for "+ name+" --> "))
        return a
    def askString(name):
        a = str(input("Enter a value for "+ name+" --> "))
        return a
    def saveObjects(file, objects):
        with open(file, "wb") as f:
            for object in objects:
                pickle.dump(object, f)
    def menu():
        print("Cabins Menu -->")
        print("----------------")
        print(" 1-Add cabins")
        print(" 2-View cabins")
        print(" 3-Available cabins")
        print(" 4-Change the estatus of a cabin")
        print(" 5-Exit")