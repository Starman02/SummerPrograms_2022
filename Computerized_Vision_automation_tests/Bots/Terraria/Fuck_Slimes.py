
from lib2to3.pgen2.token import TILDE
from multiprocessing.connection import wait
from pydoc import cli
from tkinter.messagebox import NO
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1)
print('begin')










def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    try:
        xb,yb = pyautogui.locateCenterOnScreen('D:\Summer_Programs_2021\Computerized_Vision_automation_tests\Bots\Terraria\SlimeTerraria.png',grayscale = True, confidence=.6)
        print(f'I can see it at: {xb}x{yb}')
        click(xb,yb)

    except TypeError:
        print("I Cant See")
