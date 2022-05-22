"""
This randomly selects a weapon at soon as the cool down for hits for a weapon in doom eternal. 
Example" you start the level with the shotgun, shoot it and then the game randomizes for a rocket launcher, then you shoot in and it gives you the cross bow, then you shoot again and so on, 
Made by StarMan02
"""


import random
import sys

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
    get_shooting_time



"""






class Eternal_Weapons_weaponized:


    Eternal_Weapons_Easy = {1:'Combat_shotgun', 4:"Rocket_launcher", 5:"Super_Shotgun", 6:"Ballista"}
    Eternal_Special_Weapons = {2: "Heavy_Cannon", 3:"Plasma_Rifle", 7:"Chaingun"}
    


    def __init__(self, weapon, shooting_count, shooting_time):
        self.weapon = weapon
        self.shooting_count = shooting_count
        self.shooting_time = shooting_time



    def random_weapon





    