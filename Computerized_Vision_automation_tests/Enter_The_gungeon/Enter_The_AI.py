from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)
print('begin')



# pyautogui.displayMousePosition()  



dodge_screen = pyautogui.screenshot('diabetes.png',region=(1192,592,400,400))



# main loop
def main_loop():
    
    while keyboard.is_pressed('q') == False:
        
        dodge_bullets()
        dodge_chain()
        dodge_fire()

        aim_at_basic()
        kill_shotgun()
        kill_ghost_face()
        kill_ghost_back()
        kill_knight()
        kill_slime()




    










def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)




 


    




    

    

    

    

    

    




def aim_at_basic():
    #bullet guy
    try:
        xa,ya = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Bullet_guy.png',grayscale = True, confidence=.7)
        print(f'I can see it at: {xa}x{ya}')
        click(xa,ya)
        click(xa,ya)
        click(xa,ya)
        click(xa,ya)
        click(xa,ya)

    except TypeError:
        print("No Basic Bullet Enemy")

def kill_shotgun():
    #shotgun guy
    try:
        xb,yb = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Shotgun_guy.png',grayscale = True, confidence=.7)
        print(f'I can see it at: {xb}x{yb}')
        click(xb,yb)
        click(xb,yb)
        click(xb,yb)
        click(xb,yb)
        click(xb,yb)

    except TypeError:
        print("No Shotgun Bullet")


def kill_ghost_face():
    #  ghost faced
    try:
        xgf,ygf = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Evil_ghost_face.png', confidence=.65)
        print(f'I can see it at: {xgf}x{ygf}')
        click(xgf,ygf)
        click(xgf,ygf)
        click(xgf,ygf)
        click(xgf,ygf)
        click(xgf,ygf)
    except TypeError:
        print("No Ghost Face")


def kill_ghost_back():
    # ghost back
    try:
        xgb,ygb = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\ghost_guy_back.png', confidence=.65)
        print(f'I can see it at: {xgb}x{ygb}')
        click(xgb,ygb)
        click(xgb,ygb)
        click(xgb,ygb)
        click(xgb,ygb)
        click(xgb,ygb)
    except TypeError:
        print("No Ghost Back")


def kill_knight():
    # knight face                                                    
    try:
        xkf,ykf = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Evil_knight.png', confidence=.65)
        print(f'I can see it at: {xkf}x{ykf}')
        click(xkf,ykf)
        click(xkf,ykf)
        click(xkf,ykf)
        click(xkf,ykf)
        click(xkf,ykf)
    except TypeError:
        print("No Knight Face")

    
def kill_slime():
    # slime face                                                 
    try:
        xlf,ylf = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Red_slime_gungeon.png', confidence=.65)
        print(f'I can see it at: {xlf}x{ylf}')
        click(xlf,ylf)
        click(xlf,ylf)
        click(xlf,ylf)
        click(xlf,ylf)
        click(xlf,ylf)
    except TypeError:
        print("No Knight Face")










def dodge_bullets():

    # dodge red_bullet    
    if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Bullet.png',region=(1192,592,400,400), confidence=.8) != None:
        keyboard.press("shift")
        time.sleep(.2)
        keyboard.release('shift')
        print("dodge red bullet")

    else:
        print("no red bullet")


def dodge_chain():
       #dodge chain
    if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Chain.png',region=(1192,592,400,400), confidence=.8) != None:
        keyboard.press("shift")
        time.sleep(.2)
        keyboard.release('shift')
        print("dodge chain")

    else:
        print("no chain")


def dodge_fire():
    #dodge fire
    if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Fire_dodge.png',region=(1192,592,400,400), confidence=.8) != None:
        keyboard.press("shift")
        time.sleep(.2)
        keyboard.release('shift')
        print("dodge fire")

    else:
        print("no fire")





g = main_loop()
g()