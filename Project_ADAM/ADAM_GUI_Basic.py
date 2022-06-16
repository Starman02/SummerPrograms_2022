"""
This is model one for Project ADAM's GUI Interface, which is the most basic and first GUI interface for ADAM
"""
import tkinter
import time
from ADAM_MAIN import *

class ADAM_GUI_V1:

    def __init__(self):
        self.main_window = tkinter.Tk()



        self.text_speaking_frame = tkinter.Frame(self.main_window)
        
        # this frame will have a entry box allowing the user to interact with ADAM and call specific commands
        self.entry_frame = tkinter.Frame(self.main_window)

        self.text = tkinter.StringVar()
        self.text.set("Welcome To ADAM Basic")
        

        self.label_speak = tkinter.Label(self.text_speaking_frame, textvariable = self.text)      # self.text will hold the welcome text as well as be the text for ADAM to talk back to you from

        self.entry_box = tkinter.Entry(self.entry_frame)
        self.begin_search = tkinter.Button(self.entry_frame, text="Begin Search", command= self.send_off)


        self.label_speak.pack()
        self.entry_box.pack()
        self.begin_search.pack()


        self.text_speaking_frame.pack()
        self.entry_frame.pack()






        tkinter.mainloop()

    def send_off(self):
        adam = ADAM("blank")
        retrived = str(self.entry_box.get())
        print("Sendoff")
        adam.set_entry_brain(retrived) # this sends the data off to ADAM_MAIN

        






        
        







chim = ADAM_GUI_V1()
chim



        
                                                                                                                                     