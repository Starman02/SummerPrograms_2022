"""
This randomly selects a weapon at soon as the cool down for hits for a weapon in doom eternal. 
Example" you start the level with the shotgun, shoot it and then the game randomizes for a rocket launcher, then you shoot in and it gives you the cross bow, then you shoot again and so on, 
Made by StarMan02
"""


import random






class Active_weapons_switcher:

    # this class holds the objects of the weapons number, and also stores the random number generator
    
    def __init__(self, weapon):
        self.weapon = weapon

    def random_number_generator():
        random_weapon_number = random.randint(1, 7)

        return random_weapon_number




    def generate_new_numbers(self, weapon):
        self.weapon = weapon


    def get_weapon_key(self):
        return self.weapon




