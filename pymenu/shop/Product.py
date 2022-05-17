from BasicMethods import BasicMethods

class Product:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.brand = ""
        self.stock = 0
        self.price = 0

    def setIdWP(self,id):
        self.id
    def setId(self):
        self.id = BasicMethods.askinteger("the id: ")

    def getId(self):
        return self.id

    def setName(self):
        self.name = BasicMethods.askstring("the name: ")

    def getName(self):
        return self.name

    def setPrice(self):
        self.price = BasicMethods.askinteger("the price: ")
    
    def setStock(self):
        self.stock = BasicMethods.askinteger("the stock: ")
    
    def getStock(self):
        return self.stock

    def setBrand(self):
        self.brand = BasicMethods.askstring("the brand: ")
    
    def getBrand(self):
        return self.brand

    def setPrice(self):
        self.price = BasicMethods.askinteger("the price: ")

    def getPrice(self):
        return self.price

    def print(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Brand: ", self.brand)
        print("Stock: ", self.stock)
        print("Price: ", self.price)