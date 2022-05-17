
from Person import Person


class User(Person):
    def __init__(self, first_name, last_name, email, password, phone_number):
        super().__init__(id,first_name,last_name,email,phone_number)
        self.password = password

    def get_password(self):
        return self.password
    def set_password(self,a):
        self.password = a 


