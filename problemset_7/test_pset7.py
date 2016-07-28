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

ad = Adopter('Kees', desired)
print '.... Adopter ....'
print ad.get_name()
print ad.get_desired_species()
print ad.get_score(ac)

flex = FlexibleAdopter('flexKees', desired, considered )
print
print '.... Flex adopter ....'
print flex.get_name()
print flex.get_score(ac)

print
print '.... Flearful adopter ....'

bang = FearfulAdopter('bangeJan', desired, feared)
print bang.get_score(ac)

print
print '.... Allergic adopter ....'
aa = AllergicAdopter('allergieJany', desired, considered)
print aa.get_score(ac)

aa = AllergicAdopter('allergieJany', desired, allergie)
print aa.get_score(ac)

ma = MedicatedAllergicAdopter('allergieJany', desired, allergie, meds)

print
print '.... Med Allergic adopter ....'
print ma.get_score(ac)