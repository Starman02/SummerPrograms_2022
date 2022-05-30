"""
This part of the program detects the clicks from the users mouse and then activates the weapon switcher
This will only occur when not in standby mode however
Standby mode is going to be in a while loop, and if the user has not turned on standby mode, then nothing will happen. 
when in standbymode, weapon switching will occur. 





"""



from ast import keyword
from doom_main import *
from pynput.mouse import Listener
from pynput.keyboard import Key,Controller
import time
import win32api
import sys





        


clicked = False


print("chink")

standby = True





class Simulate_clicks:

    

    random_weapon_number_generated = Active_weapons_switcher.random_number_generator()        
    i = Active_weapons_switcher(random_weapon_number_generated)
        

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
                print("shot count is: " + str(shot))
                print("weapon is: " + str(i.get_weapon_key))


                time.sleep(3)
                i.random_number_generator

                print("new number is: "+ str(i.get_weapon_key))
     
        




             


g = Simulate_clicks()
g




# presses a key
# keyword.press('key')
# keyword.release('key')