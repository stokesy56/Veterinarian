from people_class import *
from pet_class import *
from vet_class import *
from appointment_class import *
from pet_owner_class import *


# as a user can create pet
# as a user can list all appointments with corresponding pet name
# as a user i can add pet to appointment
# as a user i can get pet details and owner details from one pet

owner1 = Owner('Ron Weasley', '07234809234', 'rweasley@gmail.com', '398347523')
owner2 = Owner('Harry Potter', '072356792374', 'hpwiddasauce@hotmail.com', '134897623')
owner3 = Owner('Hermione Granger', '07976324586', 'grangerh@outlook.com', '12398746')

pet1 = Pet('Scabbers', 'Rat', owner1)
pet2 = Pet('Hedwig', 'Owl', owner2)
pet3 = Pet('Crookshanks', 'Cat', owner3)

vet1 = Vet('Dr Dumbledore', '07347863693', 'bigd@gmail.com', 'Exotic Animals')
vet2 = Vet('Dr Mcgonagall', '07234673567', 'maccyg@hotmail.com', 'Companion Animals')
vet3 = Vet('Dr Snape', '07897623483', 'snape@yahoo.com', 'Small Animals')

appointment1 = Appointment('01-10-19', '12:00', pet1, owner1, vet3)
appointment2 = Appointment('01-10-19','13:00', pet2, owner2, vet1)
appointment3 = Appointment('02-10-19','10:00', pet3, owner3, vet2)
appointment4 = Appointment('02-10-19', '12:00')
appointment5 = Appointment('02-10-19','13:00')
appointment6 = Appointment('13-10-19','10:00')

# appending appointments into list
appointment_list = []
appointment_list.append(appointment1)
appointment_list.append(appointment2)
appointment_list.append(appointment3)

# printing all appointments (including pet name)
for appointment in appointment_list:
    print('Date: ' + appointment.date + ',', 'Time: ' + appointment.time + ',', 'Pet Name: ' + appointment.pet.name + ',', 'Owner: ' + appointment.owner.name + ',', 'Vet: ' + appointment.vet.name)

#adding pet to vacant appointment
appointment4.add_pet(pet1,owner1,vet3)
appointment5.add_pet(pet2,owner2,vet1)
appointment6.add_pet(pet3,owner3,vet2)

# get pet info including owner details
print('Pet Name: ' + pet1.name + ',', 'Species: ' + pet1.species + ',', 'Owner Name: ' + pet1.owner.name + ',', 'Owner Phone: ' + pet1.owner.phone)
print('Pet Name: ' + pet2.name + ',', 'Species: ' + pet2.species + ',', 'Owner Name: ' + pet2.owner.name + ',', 'Owner Phone: ' + pet2.owner.phone)
print('Pet Name: ' + pet3.name + ',', 'Species: ' + pet3.species + ',', 'Owner Name: ' + pet3.owner.name + ',', 'Owner Phone: ' + pet3.owner.phone)

