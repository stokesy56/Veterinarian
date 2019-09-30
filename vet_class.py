from people_class import *

class Vet(People):
    def __init__(self, name, phone, email, speciality):
        super().__init__(name, phone, email)
        self.speciality = speciality
