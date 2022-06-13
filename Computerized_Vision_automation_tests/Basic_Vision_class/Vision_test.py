"""
This program will test the possibilities of computerizeds vision
RGB Of Healing Cooldown: 97, 7, 23
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1)
print('begin')
pyautogui.displayMousePosition()











# tests area for the program 

while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(584, 422, 751, 526))

    width, height = pic.size

    # for x in range(0, width, 5):
    #     for y in range(0, height, 5):

    #         r, g, b = pic.getpixel((x, y))

    #         if b == 195 and r == 255 and g == 219:
    #             flag = 1
    #             click(x+584, y+422)
    #             time.sleep(0.05)
    #             break

    #     if flag == 1:
    #         break
