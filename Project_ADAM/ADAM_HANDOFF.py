"""
This programs handles the offloading of ADAM_GUI into ADAM_MAIN
"""

class Handoff:               
    def __init__(self, placeholder=""):
        self.placeholder = placeholder          


    def get_placeholder(self):
        return self.placeholder


    def set_placeholder(self, placeholder):
        self.placeholder = placeholder