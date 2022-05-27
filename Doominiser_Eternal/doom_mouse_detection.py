"""
This part of the program detects the clicks from the users mouse and then activates the weapon switcher
This will only occur when not in standby mode however
Standby mode is going to be in a while loop, and if the user has not turned on standby mode, then nothing will happen. 
when in standbymode, weapon switching will occur. 

"""



from multiprocessing.connection import wait
from tkinter import Button
from doom_main import *
from pynput.mouse import Listener
import time

import sys


random_weapon_number_generated = Active_weapons_switcher.random_number_generator()
weapons_number = Active_weapons_switcher(random_weapon_number_generated, random_weapon_number_generated, random_weapon_number_generated)
        


clicked = False

# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')
print("chink")

standby = True




class Farty:

    click = 0

    while standby == True:

        def on_move(x, y):
            pass


        def on_scroll(x, y, dx, dy):
            pass




        def on_click(x, y, button, pressed):
            print('{0} at {1}'.format(
                'Pressed' if pressed else 'Released',
                (x, y)))
            if not pressed:
                # Stop listener
                return False


        def on_click(x, y, button, pressed):

            if pressed == True:


                random_weapon_number_generated = Active_weapons_switcher.random_number_generator()
                weapons_number = Active_weapons_switcher(random_weapon_number_generated, random_weapon_number_generated, random_weapon_number_generated)

                if weapons_number.get_weapon_number() == 2:
                    
                    print( "and so the main weapon number is: " + str(weapons_number.change_shooting_time()))

                if weapons_number.get_weapon_number() == 3:
                    print( "and so the main weapon number is: " + str(weapons_number.change_shooting_time()))

                if weapons_number.get_weapon_number() == 7:
                    print( "and so the main weapon number is: " + str(weapons_number.change_shooting_time()))

                print(("______")*10)
            else:
                pass  



    

        with Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
            listener.join()

        

    





g = Farty()
g