
# foundation for future ADAM integrations
# these parts will be a mix between ADAM_GUI and ADAM MAIN, 
# these sections will either replace the standard welcome text with displayed information, or could possibly open up more TKinter windows,
# it depends on what the user needs help with
import tkinter
from turtle import left
import pyperclip
import time
import json


class Assist_Module_MK1:
    


    def open_assistance_window(self):
        self.top_assitance = tkinter.Toplevel()

        self.test_frame = tkinter.Frame(self.top_assitance)

        # 500x100 size, first number +400 does left to right, second number(+300) does up and down
        self.top_assitance.geometry("500x100+400+300")


        self.assistance_label= tkinter.StringVar()

        self.assistance_label.set("What would you like assistance with?")

        self.label_assist_speak = tkinter.Label(self.test_frame, textvariable = self.assistance_label)  

        self.entry_box_assist = tkinter.Entry(self.test_frame)

        self.search = tkinter.Button(self.test_frame, text="Search", command = self.ADAM_ASSIST_V1)






        self.label_assist_speak.pack()
        self.entry_box_assist.pack()
        
        self.search.pack()
        self.test_frame.pack()


    def ADAM_ASSIST_V1(self):

        print("passed into")

        self.user_entry_assist = str(self.entry_box_assist.get())
        
        # for every item in the test list, do an action
        if "class" in self.user_entry_assist:
            ####################################################################################################################################################################################
            self.class_assist_window_1 = tkinter.Toplevel() # creates another window for ADAM
            self.class_frame1 = tkinter.Frame(self.class_assist_window_1)
            self.button_frame_left = tkinter.Frame(self.class_assist_window_1)

            self.class_assist_window_1.geometry('500x300+900+300')

            self.assistance_label1= tkinter.StringVar()

            self.assistance_label1.set("Help Modules")
            self.label_assist_setting = tkinter.Label(self.class_frame1, textvariable = self.assistance_label1)  
            ####
            # copy and paste storage
            #an empty dictionary
 
            ###potential idea for bigger libraries, store them in .dat files, could also be used to store them in a dictionary
            dictionary_storage = {}
            f = open('Project_ADAM\STORAGE\copy_and_paste_samples.txt', 'r')
            for line in f.readlines():
                name,action = line.split("|")
                dictionary_storage[name] = (action)
            
            self.c1 = "self."
            self.c2 = """def get_X(self):
    return self.X
             """
             
            self.c3 = """set_X(self, X):
    self.X = X"""

            # entire class demo with objects
            self.c4 = """class Demo:
    def __init(self, X):
        self.X = X
        
        
    def set_X(self, X):
        self.X = X


    def get_X(self):
        return self.X
        """
            self.c5 = """def __str__(self):
    return "the value of X is " + self.X
            """

        
            ####
            self.self_help_button = tkinter.Button(self.button_frame_left,text="Copy: self", command= lambda: self.action_button(self.c1))
            self.getter_example_button = tkinter.Button(self.button_frame_left, text="Copy: get_attribute example", command= lambda: self.action_button(self.c2))
            self.setter_example_button = tkinter.Button(self.button_frame_left, text="Copy: set_attribute example", command= lambda:self.action_button(self.c3))
            self.demo_button = tkinter.Button(self.button_frame_left, text="Copy: Class Demo", command= lambda:self.action_button(self.c4))
            self.string_returning_demo = tkinter.Button(self.button_frame_left, text="Copy: String Printing function", command= lambda:self.action_button(self.c5))



            self.label_assist_setting.pack()
            self.self_help_button.pack()
            self.getter_example_button.pack()
            self.setter_example_button.pack()
            self.string_returning_demo.pack()
            self.demo_button.pack()
            self.button_frame_left.pack(side='left')
            self.class_frame1.pack()
            ################################################################









        if "ADAM GUI" in self.user_entry_assist:
            #################################################################################################
            self.ADAMGUI_ASSIST = tkinter.Toplevel() # creates another window for ADAM
            self.ADAMGUI_frame1 = tkinter.Frame(self.ADAMGUI_ASSIST)
            self.button_frame_left2 = tkinter.Frame(self.ADAMGUI_frame1)

            self.ADAMGUI_ASSIST.geometry('500x300+900+300')

            self.assistance_label2= tkinter.StringVar()

            self.assistance_label2.set("ADAM GUI Aiding Modules")
            self.label_assist_setting2 = tkinter.Label(self.ADAMGUI_frame1, textvariable = self.assistance_label2)





            #### Storage for ADAMGUI MODULES###

            










        




            self.self_help_button = tkinter.Button(self.button_frame_left,text="Copy: self", command= lambda: self.action_button(self.c1))


































    def action_button(self, text_placeholder):
        
        pyperclip.copy(text_placeholder)
        self.assistance_label1.set("Action has been Preformed")


        






        
        
    
            
            

            


    



            
            
        
                
           
        

    


