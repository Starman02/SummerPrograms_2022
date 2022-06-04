



import tkinter as tk
import time
from PIL import ImageTk, Image

from standby_mode import Standby
import sys
import threading
from doom_mouse_detection import *


counter = 0





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
        dc = Standby()                                            # starts randomization program
        time.sleep(5)
        counter += 1


        dc.set_status(counter)

        




        
    

        







g = MainGui()
g



