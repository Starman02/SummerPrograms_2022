"""
This part of the program detects the clicks from the users mouse and then activates the weapon switcher
This will only occur when not in standby mode however
Standby mode is going to be in a while loop, and if the user has not turned on standby mode, then nothing will happen. 
when in standbymode, weapon switching will occur. 





"""



from doom_main import *
from pynput.mouse import Listener
from pynput.keyboard import Key,Controller
import time
import win32api
import sys


random_weapon_number_generated = Active_weapons_switcher.random_number_generator()
weapons_number = Active_weapons_switcher(random_weapon_number_generated, random_weapon_number_generated)


        


clicked = False


print("chink")

standby = True





class Farty:

    keyboard = Controller()


    state_left = win32api.GetKeyState(0x01)
    shot = 0




    while standby == True:
        
        shoot = win32api.GetKeyState(0x01)



        if shoot != state_left:
            state_left = shoot
            print(shoot)
            if shoot < 0:
                shot += 1
                print(shot)

                time.sleep(2)

                keyboard.press("1")
                keyboard.release("1")


                #if shot == weapons_number.get_weapon_number():


                    #win32api.keybd_event(0x35)




                 
            else:
                print('left button released')








                # if weapons_number.get_weapon_number() == 2:



                    
                #     print( "and so the main weapon number is: " + str(weapons_number.change_shooting_time()))

                # if weapons_number.get_weapon_number() == 3:
                #     print( "and so the main weapon number is: " + str(weapons_number.change_shooting_time()))

                # if weapons_number.get_weapon_number() == 7:
                #     print( "and so the main weapon number is: " + str(weapons_number.change_shooting_time()))



    





g = Farty()
g