from copyreg import pickle
import pickle

class BasicMethods:
    @staticmethod
    def askInteger(name):
        a =int(input("Enter a value for "+ name+" --> "))
        return a
    
    @staticmethod
    def askString(name):
        a = str(input("Enter a value for "+ name+" --> "))
        return a

    @staticmethod
    def saveObjects(file, objects, object):
        with open(file, "wb") as f:
            for object in objects:
                pickle.dump(object, f)
                
    def exit_program():
        print("Exiting program")
        exit()


