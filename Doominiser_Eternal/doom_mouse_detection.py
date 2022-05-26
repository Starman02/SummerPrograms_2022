"""
This part of the program detects the clicks from the users mouse and then activates the weapon switcher
This will only occur when not in standby mode however
Standby mode is going to be in a while loop, and if the user has not turned on standby mode, then nothing will happen. 
when in standbymode, weapon switching will occur. 

"""

from unittest import skip
from doom_main import *
import pyautogui
from pynput.mouse import Listener

import pygame 
import sys


# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')




def on_move(x, y):
    pass


def on_scroll(x, y, dx, dy):
    pass



def on_click(x, y, button, pressed):
    print("oh holy jebus")



with Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
    listener.join()


    




