class Cabin:

    def __init__(self, id, type, pricePerHour, availability):
        self.id = id
        self.type = type
        self.pricePerHour = pricePerHour
        self.availability = availability
    
    def get_id(self):
        return self.id
    def set_id(self,a):
        self.id = a
    def get_type(self):
        return self.type
    def set_type(self,a):
        self.type = a
    def get_pricePerHour(self):
        return self.pricePerHour
    def set_pricePerHour(self,a):
        self.pricePerHour = a
    def get_availability(self):
        return self.availability
    def set_availability(self,a):
        self.availability = a