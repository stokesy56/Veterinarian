class Appointment:
    def __init__(self, date, time, pet = '', owner = '', vet = ''):
        self.date = date
        self.time = time
        self.owner = owner
        self.pet = pet
        self.vet = vet

    def add_pet(self,pet,owner,vet):
        self.pet = pet
        self.owner = owner
        self.vet = vet
