"""
This program will test the possibilities of computerizeds vision
RGB Of Healing Cooldown: 97, 7, 23
"""

from tkinter.messagebox import NO
from pyautogui import *
import pyautogui
import time
import keyboard
import random

time.sleep(1)
print('begin')









"""
Demos for computer vision. 

"""


# tests area for the program 

while keyboard.is_pressed('q') == False:


    if pyautogui.pixelMatchesColor(2123, 43,(221 ,189 ,62)) == True:
        print("color is present")
    else:
        print("Color is not present")


    if pyautogui.locateOnScreen('healing_cooldown.png', confidence=.8) != None:
        print("ON SCREEN")

    else:
        print("NOT ON SCREEN")

    