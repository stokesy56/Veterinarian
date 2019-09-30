from people_class import *

class Owner(People):
    def __init__(self, name, phone, email, payment_details):
        super().__init__(name, phone, email)
        self.payment_details = payment_details
