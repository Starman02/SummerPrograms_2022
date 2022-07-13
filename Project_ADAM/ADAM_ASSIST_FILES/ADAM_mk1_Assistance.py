
# foundation for future ADAM integrations
# these parts will be a mix between ADAM_GUI and ADAM MAIN, 
# these sections will either replace the standard welcome text with displayed information, or could possibly open up more TKinter windows,
# it depends on what the user needs help with

import tkinter
from ADAM_class_assist_MK1 import *
import pyperclip
import pickle
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
        
        ####PUT CLASS ASSIST HERE###
        if "class" in self.user_entry_assist:
            d = Class_Assist()
            d()
        









    
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







####### required functions ################



    def action_button(self, text_placeholder):
        
        pyperclip.copy(text_placeholder)
        self.assistance_label1.set("Action has been Preformed")


    def data_window_classes(self):

        try:
            input_file = open('Project_ADAM\STORAGE\copy_paste_storage.dat', 'r+b')
            self.copy_paste_storage = pickle.load(input_file)
            input_file.close()
        except(IOError, AttributeError, EOFError):
            self.copy_paste_storage = {}
        
            


        #  initialize the first dictionary and open it
        self.__data_class_window = tkinter.Toplevel() # creates another window for ADAM
        self.__data_frame = tkinter.Frame(self.__data_class_window)

        self.data_label = tkinter.Label(self.__data_frame, text='Enter data to be copied and pasted, Be careful as the data is stored in a DAT file, making data unreadible in file form')


        self.data_key_entry = tkinter.Entry(self.__data_frame)
        self.data_entry_box = tkinter.Text(self.__data_frame, width=80, height=25)
        self.convert_data_button = tkinter.Button(self.__data_frame, text="convert text to dictionary and append to dat file", command= lambda: self.append_data_to_file())

                
            
                

        self.data_label.pack()
        self.data_key_entry.pack()
        self.data_entry_box.pack()
        self.convert_data_button.pack()
                
        self.__data_frame.pack()
    

    def append_data_to_file(self):
        self.__data_key = self.data_key_entry.get()
        self.original_DATA_entry = self.data_entry_box.get("1.0", tkinter.END)
        
        try:
            call_name = self.__data_key
            code = self.original_DATA_entry
            self.copy_paste_storage[call_name] = code
            save_to_file = open('Project_ADAM\STORAGE\copy_paste_storage.dat', "r+b")
            pickle.dump(self.copy_paste_storage, save_to_file)
            save_to_file.close()
        except FileNotFoundError:
            save_to_file = open('Project_ADAM\STORAGE\copy_paste_storage.dat', "wb")
            pickle.dump(self.copy_paste_storage, save_to_file)
            save_to_file.close()

        print('action preformed')
            
        
        

        

    



                


        






        
        
    
            
            

            


    



            
            
        
                
           
        

    


