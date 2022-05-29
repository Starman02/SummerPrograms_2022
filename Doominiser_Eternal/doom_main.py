"""
This randomly selects a weapon at soon as the cool down for hits for a weapon in doom eternal. 
Example" you start the level with the shotgun, shoot it and then the game randomizes for a rocket launcher, then you shoot in and it gives you the cross bow, then you shoot again and so on, 
Made by StarMan02
"""


import random






class Active_weapons_switcher:
    def __init__(self, weapon, shooting_count, shooting_time):
        self.weapon = weapon
        self.shooting_count = shooting_count
        self.shooting_time = shooting_time



    def random_number_generator():
        random_weapon_number = random.randint(1, 7)

        return random_weapon_number



    def change_shooting_time(self):

        if self.shooting_time == 2:
            self.shooting_time = 3.5
        
        elif self.shooting_time == 3:
            self.shooting_time = 4.89

        elif self.shooting_time == 7:
            self.shooting_time = 9.5

        

        return self.shooting_time

    
    def change_shooting_count(self):

        temporary = self.shooting_count

        if temporary == 1:
            self.shooting_count = 1
            
        elif temporary == 4:
            self.shooting_count = 11

        elif temporary == 5:
            self.shooting_count = 111

        elif temporary == 6:
            self.shooting_count = 1111

        return self.shooting_count


    def get_weapon_number(self):
        return self.weapon


    def get_weapon_name(self):

        if self.weapon == 1:
            self.weapon = "Combat Shotgun"
        elif self.weapon == 2:
            self.weapon = "Heavy Cannon"
        elif self.weapon == 3:
            self.weapon = "Plasma Rifle"
        elif self.weapon == 4:
            self.weapon = "Rocket Launcher"
        elif self.weapon == 5:
            self.weapon = "Super Shotgun"
        elif self.weapon == 6:
            self.weapon = "Ballista"
        elif self.weapon == 7:
            self.weapon = "Chaingun" 

        return self.weapon


    def get_shooting_time(self):
        return self.shooting_time


    def get_shooting_count(self):
        return self.shooting_count

    def __str__(self):
        main_printings = str(self.weapon) + " Weapon selection " + str(self.shooting_count) + " weapon Shooting Count " + str(self.shooting_time) + " weapon Shooting Time"
        return main_printings

    def random_number_generator():
        random_weapon_number = random.randint(1, 7)

        return random_weapon_number






random_weapon_number_generated = Active_weapons_switcher.random_number_generator()
weapons_number = Active_weapons_switcher(random_weapon_number_generated, random_weapon_number_generated, random_weapon_number_generated)




# gives the sorter a random number
# will be moved into main function


# assigns random numbers into the generator
# should probobly put them in a function


print("poverty")

# these just print the numbers to be generated
print( "and so the main weapon number is: " + str(weapons_number.get_weapon_name()))
print( "the count number is: " + str(weapons_number.change_shooting_count()))
print( "the time number is: " + str(weapons_number.change_shooting_time()))
    