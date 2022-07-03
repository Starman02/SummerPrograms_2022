# foundation for future ADAM integrations
# these parts will be a mix between ADAM_GUI and ADAM MAIN, 
# these sections will either replace the standard welcome text with displayed information, or could possibly open up more TKinter windows,
# it depends on what the user needs help with
from curses import tigetflag
import tkinter
import pyperclip
import time


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
            self.class_assist_window_1 = tkinter.Toplevel() # creates another window for ADAM
            self.class_frame1 = tkinter.Frame(self.class_assist_window_1)

            self.class_assist_window_1.geometry('500x300+900+300')

            self.assistance_label1= tkinter.StringVar()

            self.assistance_label1.set("Help Modules")
            self.label_assist_setting = tkinter.Label(self.class_frame1, textvariable = self.assistance_label1)  
            ####
            # copy and paste storage
            self.c1 = "self."
            self.c2 = ("")
            ####
            self.self_help_button = tkinter.Button(self.class_assist_window_1,text="Copy: self", command= lambda: self.action_button(self.c1))
            self.getter_example_button = tkinter.Button(self.class_assist_window_1, text="Copy: get_attribute example")
            self.setter_example_button = tkinter.Button(self.class_assist_window_1, text="Copy: set_attribute example")



            self.label_assist_setting.pack()
            self.self_help_button.pack(side="left")
            self.class_frame1.pack()


    def action_button(self, text_placeholder):
        
        pyperclip.copy(text_placeholder)
        self.assistance_label1.set(text_placeholder + " Action has been Preformed")


        



        
        
    
            
            

            


    



            
            
        
                
           
        

    


