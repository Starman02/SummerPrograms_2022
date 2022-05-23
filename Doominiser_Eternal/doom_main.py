"""
This randomly selects a weapon at soon as the cool down for hits for a weapon in doom eternal. 
Example" you start the level with the shotgun, shoot it and then the game randomizes for a rocket launcher, then you shoot in and it gives you the cross bow, then you shoot again and so on, 
Made by StarMan02
"""


import random
import re
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






class Eternal_Weapons_weaponized:


    Eternal_Weapons_Easy = {1:'Combat_shotgun', 2: "Heavy_Cannon", 3:"Plasma_Rifle", 4:"Rocket_launcher", 5:"Super_Shotgun", 6:"Ballista",  7:"Chaingun"}
    Eternal_Special_Weapons = {2: "Heavy_Cannon", 3:"Plasma_Rifle", 7:"Chaingun"}
    


    def __init__(self, weapon = 0, shooting_count = 0, shooting_time = 0):
        random_weapon_number = random.randint(1, 7)
        self.weapon = random_weapon_number
        self.shooting_count = random_weapon_number
        self.shooting_time = random_weapon_number
        

        

    def set_shooting_count(self, shooting_count):

            if self.__weapon == 1:
                print(self.__weapon)
                shooting_count = 1
            
            elif self.__weapon == 4:
                print(self.__weapon)
                shooting_count = 11

            elif self.__weapon == 5:
                print(self.__weapon)
                shooting_count = 111

            elif self.__weapon == 6:
                print(self.__weapon)
                shooting_count = 1111

            
            self.shooting_count = shooting_count


    def get_shooting_count(self):
            return self.shooting_count






    def set_shooting_time(self, shooting_time):

        if self.weapon == 2:
            print(self.weapon)
            shooting_time = 3.5
        
        elif self.weapon == 3:
            print(self.weapon)
            shooting_time = 6

        elif self.weapon == 7:
            print(self.weapon)
            shooting_time = 9.5
        
        self.__shooting_time = shooting_time



    def get_shooting_time(self):
        return self.shooting_time


    


   


    
    def __str__(self):
        main_printins = str(self.weapon) + " shotgun blasttttt " + str(self.shooting_count) + "   Shotgungolongus   " +str(self.shooting_time)
        return main_printins
        
    




    




my_squizzle = Eternal_Weapons_weaponized()
print(my_squizzle)








        
        
    












































# def start_randomized_mode():
#     standby = True

#     while standby == True:
#         # programs logic to click and swap







# start_game()

    