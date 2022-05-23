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
    random_weapon_number = random.randint(1, 7)
    


    def __init__(self, weapon = random_weapon_number, shooting_count = random_weapon_number, shooting_time = random_weapon_number):
        
        self.__weapon = weapon
        self.__shooting_count = shooting_count
        self.__shooting_time = shooting_time
        

        

    def set_shooting_count(self, shooting_count):

            if shooting_count == 1:
                print(shooting_count)
                shooting_count = 1
            
            elif shooting_count == 4:
                print(shooting_count)
                shooting_count = 11

            elif shooting_count == 5:
                print(shooting_count)
                shooting_count = 111

            elif shooting_count == 6:
                print(shooting_count)
                shooting_count = 1111

            
            Eternal_Weapons_weaponized.set_shooting_count(shooting_count)


    def get_shooting_count(self):
            return self.__shooting_count


    def set_shooting_time(self, shooting_time):

        if shooting_time == 2:
            print(shooting_time)
            self.__shooting_time = 3.5
        
        elif shooting_time == 3:
            print(shooting_time)
            self.__shooting_time = 6

        elif shooting_time == 7:
            print(shooting_time)
            self.__shooting_time = 9.5

        Eternal_Weapons_weaponized.get_shooting_count()

        

        



    def get_shooting_time(self):
        return self.__shooting_time


    


   


    
    def __str__(self):
        main_printins = str(self.__weapon) + " shotgun blasttttt " + str(self.__shooting_count) + "   Shotgungolongus   " +str(self.__shooting_time)
        return main_printins
        
    




    




my_squizzle = Eternal_Weapons_weaponized()
print(my_squizzle)








        
        
    












































# def start_randomized_mode():
#     standby = True

#     while standby == True:
#         # programs logic to click and swap







# start_game()

    