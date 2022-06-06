



import tkinter as tk
import time
from PIL import ImageTk, Image
import sys
from doom_main import *
from pynput.mouse import Listener
from pynput.keyboard import Key,Controller
import time
import win32api
# from doom_mouse_detection import *


counter = 0






    

    







class Slaying_and_praying:


    def __init__(self, if_counted=0):
        self.if_counted = if_counted

    
    
    # sets and gets standby status for the 
    def start_game(self, if_counted):
        self.if_counted = if_counted
        print(str(self.if_counted))
        self.start_slaying()


    def get_if_counted(self):
        return self.if_counted


    
    def start_slaying(self):
        print("in function")
        random_weapon_number_generated = Active_weapons_switcher.random_number_generator()        
        i = Active_weapons_switcher(random_weapon_number_generated)      
        keyboarded = Controller()




        state_left = win32api.GetKeyState(0x01)
                                                            
        standby = True
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
                        time.sleep(1.5)

                        keyboarded.press(str(a))
                        keyboarded.release(str(a))
                        i.generate_new_numbers(Active_weapons_switcher.random_number_generator())
                    else:
                        pass
        

class MainGui:
    
    

    def __init__(self):
        self.gui_window = tk.Tk()

        
        self.gui_window.geometry("800x900")
        self.gui_window.title("The Randomizer Slayer")


        self.img = ImageTk.PhotoImage(file="D:\Summer_Programs_2021\SummerPrograms_2022\Doominiser_Eternal\Damone_moutain.png")
        # background pane



        #create canvas

        self.canvas = tk.Canvas(self.gui_window, width=800, height=900)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_image(0,0, image=self.img, anchor="nw")

        #intro label that goes over image
        self.canvas.create_text(400, 150, text="Begin Randomized Slaying", font=("Helvetica", 45), fill="white")

        # status button (displays current weapon)
        self.canvas.create_text(378, 804, text="Current weapon is: ", font=("Helvetica", 10), fill="white")



        # button to start the game
        start_button = tk.Button(self.gui_window, text="Rip & Randomized", height=30, width=50, bg="orange", command=self.start_randomization)
        start_button_window = self.canvas.create_window(393, 426, anchor="center", window=start_button)

        
        


        # frames for text to go over frames


        
        # label for title

        self.gui_window.mainloop()
    


  
   
    
    def start_randomization(self):  
        ab = Slaying_and_praying()
        time.sleep(5)
        print('begining')
        ab.start_game(1)

        
        


        

g = MainGui()
g

