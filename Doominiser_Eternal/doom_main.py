"""
This randomly selects a weapon at soon as the cool down for hits for a weapon in doom eternal. 
Example" you start the level with the shotgun, shoot it and then the game randomizes for a rocket launcher, then you shoot in and it gives you the cross bow, then you shoot again and so on, 
Made by StarMan02
"""


import random






class Active_weapons_switcher:
    def __init__(self, weapon):
        self.weapon = weapon



    def random_number_generator():
        random_weapon_number = random.randint(1, 7)

        return random_weapon_number



    def change_shooting_key(self):

        if self.shooting_count == 1:
            self.shooting_count = 1
            
        elif self.shooting_count == 4:
            self.shooting_count = 4

        elif self.shooting_count == 5:
            self.shooting_count = 5

        elif self.shooting_count == 6:
            self.shooting_count = 6





    def get_weapon_key(self):

        # if self.weapon == 1:
        #     self.weapon = 1
        # elif self.weapon == 2:
        #     self.weapon = 2
        # elif self.weapon == 3:
        #     self.weapon = 3
        # elif self.weapon == 4:
        #     self.weapon = 4
        # elif self.weapon == 5:
        #     self.weapon = 5
        # elif self.weapon == 6:
        #     self.weapon = 6
        # elif self.weapon == 7:
        #     self.weapon = 7

        return self.weapon


    def __str__(self):
        main_printings = str(self.weapon) + " Weapon selection " + str(self.shooting_count) + " weapon Shooting Count " + str(self.shooting_time) + " weapon Shooting Time"
        return main_printings








# gives the sorter a random number
# will be moved into main function


# assigns random numbers into the generator
# should probobly put them in a function


print("poverty")

# # these just print the numbers to be generated
# print( "and so the main weapon number is: " + str(weapons_number.get_weapon_name()))
# print( "the count number is: " + str(weapons_number.change_shooting_count()))
# print( "the time number is: " + str(weapons_number.change_shooting_time()))
    