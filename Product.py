from BasicMethods import BasicMethods

class Product:
    def __init__(self, id, name, brand, price, stock):
        self.id = id
        self.name = name
        self.brand = brand
        self.stock = stock
        self.price = price

    def setIdWP(self,id):
        self.id
    def setId(self):
        self.id = BasicMethods.askInteger("the id: ")

    def getId(self):
        return self.id

    def setName(self):
        self.name = BasicMethods.askString("the name: ")

    def getName(self):
        return self.name

    def setPrice(self):
        self.price = BasicMethods.askInteger("the price: ")
    
    def setStock(self):
        self.stock = BasicMethods.askInteger("the stock: ")
    
    def getStock(self):
        return self.stock

    def setBrand(self):
        self.brand = BasicMethods.askString("the brand: ")
    
    def getBrand(self):
        return self.brand

    def setPrice(self):
        self.price = BasicMethods.askInteger("the price: ")

    def getPrice(self):
        return self.price

    def print(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Brand: ", self.brand)
        print("Stock: ", self.stock)
        print("Price: ", self.price)