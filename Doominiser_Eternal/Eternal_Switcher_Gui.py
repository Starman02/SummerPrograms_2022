

import tkinter as tk
from PIL import ImageTk, Image








class MainGui:
    def __init__(self):
        self.gui_window = tk.Tk()

        self.gui_window.geometry("800x900")
        self.gui_window.configure(background='gray')

        self.img = ImageTk.PhotoImage(file="D:\Summer_Programs_2021\SummerPrograms_2022\Doominiser_Eternal\senorDoomington.png")
        # background panel
        self.bgpanel = tk.Label(self.gui_window, image=self.img)
        self.bgpanel.pack(side='bottom', fill="both", expand="yes")



        self.gui_window.mainloop()


        
    

        







g = MainGui()
g



