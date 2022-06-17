"""
Project ADAM's Main class, this will retrive data from other main questions/categories/questions
"""

import tkinter
from ADAM_mk1_Assistance import *




class ADAM: 
    def __init__(self, command_adam):
        self.command_adam = command_adam



    def set_entry_brain(self, command_adam):
        self.command_adam = str(command_adam)
        Adam_gui = ADAM_GUI_V1()
        Adam_gui.text.set("Hello, What kind of Decision do you need help with?")

        if command_adam == "decision help":
            adam_assist = ADAM_Decision_assist_v0()
            adam_assist.start_assistance_mk1()

            
        




    # basic first attributes
    # 1. Query Type(Assistance?,Decision making asistance?, )

        
        

