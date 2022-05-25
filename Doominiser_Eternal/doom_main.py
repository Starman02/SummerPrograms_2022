"""
This randomly selects a weapon at soon as the cool down for hits for a weapon in doom eternal. 
Example" you start the level with the shotgun, shoot it and then the game randomizes for a rocket launcher, then you shoot in and it gives you the cross bow, then you shoot again and so on, 
Made by StarMan02
"""


import random
import sys



standby = False

"""

class= weapons_randomized
    init-
        Weapon
        Shooting_count
        Shootin_time


        ######
    setters
    get_Weapons
    set_shooting_count
    set_shooting_time

    get_shooting_count
    get_shooting_timeSAVED



"""

random_weapon_number = random.randint(1, 7)


# class Eternal_Weapons_options:

#     def __init__(self, weapon_number, shooting_count_number, shooting_time_number):
#         self.weapon_number = weapon_number
#         self.shooting_count_number = shooting_count_number
#         self.shooting_time_number = shooting_time_number



#     def __str__(self):
#         main_printings = str(self.weapon_number) + " Weapon Count " + str(self.shooting_count_number) + " Shooting Count " + str(self.shooting_time_number) + " Shooting Time"
#         return main_printings


def random_number_generator():
    random_weapon_number = random.randint(1, 7)

    return random_weapon_number





class Active_weapons_switcher:
    def __init__(self, weapon, shooting_count, shooting_time):
        self.weapon = weapon
        self.shooting_count = shooting_count
        self.shooting_time = shooting_time
        self.__random_number_generator = None


    # thats called motha fuckin bars

    def change_shooting_time(self):  
        if self.shooting_time == 2:
            self.shooting_time = 3.5
        
        elif self.shooting_time == 3:
            self.shooting_time = 6

        elif self.shooting_time == 7:
            self.shooting_time = 9.5

        return self.shooting_time

    
    def change_shooting_count(self):
        if self.shooting_time == 1:
            self.shooting_time = 1
            
        elif self.shooting_count == 4:
            self.shooting_count = 111

        elif self.shooting_count == 5:
            self.shooting_time = 111

        elif self.shooting_count == 6:
            self.shooting_count = 1111

        return self.shooting_count



    def get_weapon_number(self):
        return self.weapon



    def get_shooting_time(self):
        return self.shooting_time


    def get_shooting_count(self):
        return self.shooting_count

    def __str__(self):
        main_printings = str(self.weapon) + " Weapon selection " + str(self.shooting_count) + " weapon Shooting Count " + str(self.shooting_time) + " weapon Shooting Time"
        return main_printings
        
    
    


        









# gives the sorter a random number
# will be moved into main function

random_weapon_number_generated = random_number_generator()
weapons_number = Active_weapons_switcher(random_weapon_number_generated, random_weapon_number_generated, random_weapon_number_generated)

print( "and so the main weapon number is: " + str(weapons_number.get_weapon_number()))
print( "the count number is: " + str(weapons_number.change_shooting_count()))
print( "the time number is: " + str(weapons_number.change_shooting_time()))








# def start_randomized_mode():
#     standby = True

#     while standby == True:
#         # programs logic to click and swap







# start_game()

    