

import tkinter as tk
from PIL import ImageTk, Image








class MainGui:
    def __init__(self):
        self.gui_window = tk.Tk()

        self.gui_window.geometry("800x900")
        self.gui_window.title("The Randomizer Slayer")


        self.img = ImageTk.PhotoImage(file="D:\Summer_Programs_2021\SummerPrograms_2022\Doominiser_Eternal\Damone_moutain.png")
        # background panel
        self.bgpanel = tk.Label(self.gui_window, image=self.img)
        


        # frames for text to go over frames
        self.title_frame = tk.Frame(self.gui_window)
        self.button_frame = tk.Frame(self.gui_window) # this frame will also display the status of the gun
        self.bottom_frame = tk.Frame(self.gui_window)  # this frame will display my name and also potentially a donation box


        
        # label for title
        self.title_lable = tk.Label(self.title_frame, text="test text")


        self.title_lable.pack()

        self.title_frame.pack()
        self.button_frame.pack()
        self.bottom_frame.pack()
        self.bgpanel.pack(side='bottom', fill="both", expand="yes")
        self.gui_window.mainloop()


        
    

        







g = MainGui()
g



