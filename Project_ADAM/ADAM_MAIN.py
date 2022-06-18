"""
Project ADAM's Main class, this will retrive data from other main questions/categories/questions
"""

import tkinter
from ADAM_mk1_Assistance import *
from ADAM_GUI_Basic import *
from ADAM_HANDOFF import Handoff

placeholder = Handoff()



class ADAM_V1: 
    

    def __init__(self, command_adam):
        self.command_adam = placeholder.get_placeholder()





    def set_entry_brain(self, command_adam):
        self.command_adam = str(command_adam)
        Adam_gui = ADAM_GUI_V1()
        Adam_gui.ADAM_LABEL.set("Hello, What kind of Decision do you need help with?")

        if self.command_adam == "decision help":
            print("need assistance?")

           

            
        




    # basic first attributes
    # 1. Query Type(Assistance?,Decision making asistance?, )

        
        

