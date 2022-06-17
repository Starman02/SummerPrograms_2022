# foundation for future ADAM integrations
# these parts will be a mix between ADAM_GUI and ADAM MAIN, 
# these sections will either replace the standard welcome text with displayed information, or could possibly open up more TKinter windows,
# it depends on what the user needs help with
from ADAM_GUI_Basic import *

class ADAM_Decision_assist_v0:                     
    def __init__(self, assistance):
        self.assistance = assistance          


    def get_assistance(self):
        return self.assistance

    def set_assistance(self, assistance):
        self.assistance = assistance

    def start_assistance_mk1(self):
        ADAM_gui = ADAM_GUI_V1()
        ADAM_gui.ADAM_LABEL.set("grimble")


    

    


