from copyreg import pickle
import pickle

class BasicMethods:
    def askInteger(name):
        a =int(input("Enter a value for "+ name+" --> "))
        return a
    def askString(name):
        a = str(input("Enter a value for "+ name+" --> "))
        return a
    def saveObjects(file, objects, object):
        with open(file, "wb") as f:
            for object in objects:
                pickle.dump(object, f)
