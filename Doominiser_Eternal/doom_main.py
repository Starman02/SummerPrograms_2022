"""
This randomly selects a weapon at soon as the cool down for hits for a weapon in doom eternal. 
Example" you start the level with the shotgun, shoot it and then the game randomizes for a rocket launcher, then you shoot in and it gives you the cross bow, then you shoot again and so on, 
Made by StarMan02
"""


import random
import re
import sys
from turtle import st


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


class Eternal_Weapons_options:
    def __init__(self, weapons = random_weapon_number, shooting_count = random_weapon_number , shooting_time = random_weapon_number):
        self.__weapons = weapons
        self.__shooting_count = shooting_count
        self.__shooting_time = shooting_time

    
    def set_weapon(self, weapons):
        self.__weapons = weapons

    
    def set_shooting_count(self, shooting_count):
        self.__shooting_count = shooting_count

    
    def set_shooting_time(self, shooting_time):
        self.__shooting_time = shooting_time



<<<<<<< HEAD
            
            Eternal_Weapons_weaponized.set_shooting_count(shooting_count)
=======
    def get_weapon(self):
        return self.__weapons  
>>>>>>> 6b6d14d96eef17d66135c23b514ae11d7306827f


    def get_shooting_count(self):
        return self.__shooting_count                               


    def get_shooting_time(self):
        return self.__shooting_time  


<<<<<<< HEAD
=======







class Active_weapons:

    # call eternal weapons and randomize them here


    # whatya looking at?




    
       








    def set_shooting_count(self, shoot_counting):


        if self.shooting_count == 1:
            shoot_counting = 1
            
        elif self.shooting_count == 4:
            shoot_counting = 11

        elif self.shooting_count == 5:
            shoot_counting = 111

        elif self.shooting_count == 6:
            shoot_counting = 1111
    
>>>>>>> 6b6d14d96eef17d66135c23b514ae11d7306827f
    def set_shooting_time(self, shooting_time):

        if shooting_time == 2:
            print(shooting_time)
<<<<<<< HEAD
            self.__shooting_time = 3.5
        
        elif shooting_time == 3:
            print(shooting_time)
            self.__shooting_time = 6

        elif shooting_time == 7:
            print(shooting_time)
            self.__shooting_time = 9.5

        Eternal_Weapons_weaponized.get_shooting_count()
=======
            self.shooting_time = 3.5
        
        elif shooting_time == 3:
            print(shooting_time)
            self.shooting_time = 6

        elif shooting_time == 7:
            print(shooting_time)
            self.shooting_time = 9.5

        
        Eternal_Weapons.__setattr__(self, self.shoot_time, shooting_time)

>>>>>>> 6b6d14d96eef17d66135c23b514ae11d7306827f

        

        



    def get_shooting_time(self):
        return self.shooting_time




    
    def __str__(self):
        gangsta = Eternal_Weapons()

        main_printings = str(self.weapon) + " Weapon Count " + str(self.shoot_counting) + " Shooting Count " + str(self.shoot_time) + " Shooting Time"
        return main_printings
        
    




    




my_squizzle = Eternal_Weapons()
print(my_squizzle)








        
        
    












































# def start_randomized_mode():
#     standby = True

#     while standby == True:
#         # programs logic to click and swap







# start_game()

    