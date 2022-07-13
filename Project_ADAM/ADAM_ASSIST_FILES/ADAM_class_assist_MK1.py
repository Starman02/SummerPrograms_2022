import tkinter
import pyperclip
import pickle
import time
import json

class Class_Assist:
    def class_assist(self):
                
                    ####################################################################################################################################################################################
        self.class_assist_window_1 = tkinter.Toplevel() # creates another window for ADAM
        self.class_frame1 = tkinter.Frame(self.class_assist_window_1)
        self.button_frame_left = tkinter.Frame(self.class_assist_window_1)
        self.data_entry_frame = tkinter.Frame(self.class_assist_window_1)

        self.class_assist_window_1.geometry('500x300+900+300')

        self.assistance_label1= tkinter.StringVar()

        self.assistance_label1.set("Help Modules")
        self.label_assist_setting = tkinter.Label(self.class_frame1, textvariable = self.assistance_label1)  
        ####
        # copy and paste storage
        #an empty dictionary

        ###potential idea for bigger libraries, store them in .dat files, could also be used to store them in a dictionary
        
        
        # load Data file into copy_paste storage
        try:
            file_open= open('Project_ADAM\STORAGE\copy_paste_storage.dat', 'rb')
            self.copy_paste_storage = pickle.load(file_open)
            file_open.close()
        except:
            print("excepted")
            self.copy_paste_storage = {}
        
        # gets self.
        try:
            self.c1 = self.copy_paste_storage['c1']
        except:
            print("Key Not Recognized")


        try:
            self.c2 = self.copy_paste_storage['c2']
        except:
            print("Key Not Recognized")
        
        try:
            self.c3 = self.copy_paste_storage['c3']
        except:
            print("Key Not Recognized")

        
        try:
            self.c4 = self.copy_paste_storage['c4']
        except:
            print("Key Not Recognized")

        # entire class demo with objects

        try:
            self.c5 = self.copy_paste_storage['c5']
        except:
            print("Key Not Recognized")


        ####
        self.self_help_button = tkinter.Button(self.button_frame_left,text="Copy: self", command= lambda: self.action_button(self.c1))
        self.getter_example_button = tkinter.Button(self.button_frame_left, text="Copy: get_attribute example", command= lambda: self.action_button(self.c2))
        self.setter_example_button = tkinter.Button(self.button_frame_left, text="Copy: set_attribute example", command= lambda:self.action_button(self.c3))
        self.demo_button = tkinter.Button(self.button_frame_left, text="Copy: Class Demo", command= lambda:self.action_button(self.c4))
        self.string_returning_demo = tkinter.Button(self.button_frame_left, text="Copy: String Printing function", command= lambda:self.action_button(self.c5))
        
        self.open_data_entry_window = tkinter.Button(self.data_entry_frame, text='Open data window', command= lambda: self.data_window_classes())



        self.label_assist_setting.pack()
        self.self_help_button.pack()
        self.getter_example_button.pack()
        self.setter_example_button.pack()
        self.string_returning_demo.pack()
        self.open_data_entry_window.pack(side='bottom')
        self.demo_button.pack()
        self.class_frame1.pack()
        self.button_frame_left.pack(side='left')
        self.data_entry_frame.pack(side='bottom')
        


        

        

                    ################################################################