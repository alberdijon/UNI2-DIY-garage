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
            return True
        if a==0:
            return False
        else:
            print("Wrong value, please repeat the process")
    
        
