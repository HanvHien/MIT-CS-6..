import random 
import string


class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method 
    to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        # Your Code Here
        self.name = name
        self.species_types = species_types
        self.location = (float(location[0]), float(location[1]))

    def get_number_of_species(self, animal):
        # Your Code Here
        return (self.species_types[animal] 
            if animal in self.species_types 
            else 0)

    def get_location(self):
        # Your Code Here
        return self.location

    def get_species_count(self):
        # Your Code Here
        return self.species_types.copy()

    def get_name(self):
        # Your Code Here
        return self.name

    def adopt_pet(self, species):
        # Your Code Here
        if species in self.species_types:
            self.species_types[species] -= 1
            if self.species_types[species] == 0:
                self.species_types.pop(species)



class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        # Your Code Here
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        # Your Code Here
        return self.name

    def get_desired_species(self):
        # Your Code Here
        return self.desired_species

    def get_score(self, adoption_center):
        # Your Code Here
        score = 1.0 * adoption_center.get_number_of_species(self.get_desired_species())
        return (score if score > 0 else 0) 



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):

        score_desired = 1.0 * Adopter.get_score(self,adoption_center)
        other_animals = adoption_center.get_species_count()
        considered = self.considered_species
        som = 0.3 * sum([other_animals[c]  for c in considered if c in other_animals])
        return score_desired + som


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        s1 = 1 * Adopter.get_score(self, adoption_center)
        s2 = adoption_center.get_number_of_species(self.feared_species)

        som = s1 - 0.3 * s2
        return max(som, 0.0)

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        s1 = Adopter.get_score(self, adoption_center)
        other_animals = adoption_center.get_species_count()
        mul = 1
        for al in self.allergic_species:
            if al in other_animals:
                mul = 0
        return mul * s1



class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        s1 = Adopter.get_score(self, adoption_center)
        other_animals = adoption_center.get_species_count()
        mul = []
        for al in self.allergic_species: 
            if al in other_animals:
                mul.append(self.medicine_effectiveness[al]) 

        m = 0
        if mul == []:
            m = 1
        else:
            m = min(mul)

        return m * s1

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.

    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = (float(location[0]), float(location[1]))

    def get_linear_distance(self, to_location):
        x1 = self.location[0]
        y1 = self.location[1]

        x2 = to_location[0]
        y2 = to_location[1]

        linDist = ((x2-x1)**2  + (y2 - y1)**2)**(0.5)

        return linDist

    def get_score(self, adoption_center):
        baseScore = Adopter.get_score(self, adoption_center)
        distance = self.get_linear_distance(adoption_center.get_location())

        if distance < 1:
            mul = 1
        elif distance < 3:
            mul = random.uniform(0.7, 0.9)
        elif distance < 5:
            mul = random.uniform(0.5, 0.7)
        else:
            mul = random.uniform(0.1, 0.5)

        return mul * baseScore



def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here 
    
    ll = [[l , adopter.get_score(l)] for l in list_of_adoption_centers]
    ll.sort(key=lambda x : (-x[1], x[0].get_name()))
    oacl = [l[0] for l in ll ]
    return oacl

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 
    ll = [[l, l.get_score(adoption_center)] for l in list_of_adopters ]
    ll.sort(key=lambda x : (-x[1], x[0].get_name()))
    oacl = [l[0] for l in ll ]
    
    return oacl