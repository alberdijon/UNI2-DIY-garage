

from Person import *



class Employee (Person):

    def __init__(self,id,first_name,last_name,email,phone_number,job,salary):

        super().__init__(id,first_name,last_name,email,phone_number)
        self.job=job
        self.salary=salary


        def get_job(self):
            return self.job
        def set_job(self,a):
            self.job=a
        def get_salary(self):
            return self.job
        def set_salary(self,a):
            self.salary=a

            

    