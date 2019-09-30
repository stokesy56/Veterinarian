class Appointment:
    def __init__(self, date, time, pet_name, owner, vet_name):
        self.date = date
        self.time = time
        self.owner = owner
        self.pet_name = pet_name
        self.vet_name = vet_name

    def appt_details(self):
        appt_details = {
            'date': self
        }