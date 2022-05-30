"""
This is the main GUI for the program, its controls the opepening and starting of the program


Click on this to start the GUI side of the program.


"""


import tkinter
import tkinter.font as tkfont

class Eternal_weapon_switcher:

    def __init__(self):
        self.main_window = tkinter.Tk()
        #fonting
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=30)
        self.main_window.geometry("900x900")


        # main frame groups
        self.title_frame = tkinter.Frame()
        self.button_start_frame = tkinter.Frame()
        # should have a check box to disable all guns

        self.bottom_frame = tkinter.Frame()
        # store paypal button and @ label


        # title frame widgets
