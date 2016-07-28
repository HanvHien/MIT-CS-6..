from ps7_skeleton import *

ac_name = 'Han'
ac_loc = (5, 5)
animals = {"Dog": 10, "Cat": 5, "Lizard": 100, "Horse": 8}
ac = AdoptionCenter(ac_name, animals, ac_loc)
desired = 'Cat'
considered = ['Dog', 'Lion']
allergie = ['Dog', 'Horse']
feared = 'Lizard'
meds = {"Dog": 0.5, "Cat": 0.0, "Horse": 1.0}

print ac.get_name()
print ac.get_location()
print ac.get_number_of_species(desired)
print ac.get_species_count()



sl = SluggishAdopter('Sluggi', desired , (0,0))

print sl.get_linear_distance(ac.get_location())
print sl.get_score(ac)