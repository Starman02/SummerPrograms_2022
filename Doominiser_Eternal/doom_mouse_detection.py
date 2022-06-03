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
import keyboard






standby = False













class Simulate_clicks:

    print("chunk")




    random_weapon_number_generated = Active_weapons_switcher.random_number_generator()        
    i = Active_weapons_switcher(random_weapon_number_generated)

    

    keyboarded = Controller()




    state_left = win32api.GetKeyState(0x01)
    
 

    while standby == True:
            
        shoot = win32api.GetKeyState(0x01)




        if shoot != state_left:
            state_left = shoot
                
            print("detected mouse")
            if shoot > 0:
                a = i.get_weapon_key()
                if a == 1 or a == 4 or a == 5 or a == 6:
                    print("short")
                    time.sleep(.5)
                        
                    keyboarded.press(str(a))
                    keyboarded.release(str(a))
                    i.generate_new_numbers(Active_weapons_switcher.random_number_generator())
                    print("New Gun is: " + str(i.get_weapon_key()))
                else:
                    pass

            elif shoot < 0:
                print("release mouse")
                    
                a = i.get_weapon_key()

                if a == 2 or a == 3 or a == 7:
                    print("long")
                    time.sleep(3)

                    keyboarded.press(str(a))
                    keyboarded.release(str(a))
                    i.generate_new_numbers(Active_weapons_switcher.random_number_generator())
                else:
                    pass


                
                    


                

                    

                

                

                    



     
        




             








# presses a key
# keyword.press('key')
# keyword.release('key')