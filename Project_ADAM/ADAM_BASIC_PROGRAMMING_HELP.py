import tkinter
import pyperclip
import pickle
import time
import json

class Basic_programing_Assist:

    
    def class_assist_start1(self):
                
                    ####################################################################################################################################################################################
        self.programming_window = tkinter.Toplevel() # creates another window for ADAM
        self.assist_basic_frame = tkinter.Frame(self.programming_window)
        self.button_frame_left2 = tkinter.Frame(self.programming_window)
        # potential explanation window
        self.data_entry_frame1 = tkinter.Frame(self.programming_window)

        self.programming_window.geometry('500x300+900+300')

        self.assistance_label2= tkinter.StringVar()

        self.assistance_label2.set("Help Modules")
        self.label_assist_setting1 = tkinter.Label(self.assist_basic_frame, textvariable = self.assistance_label2)  
        ####
        # copy and paste storage
        #an empty dictionary

        ###potential idea for bigger libraries, store them in .dat files, could also be used to store them in a dictionary
        
        
        # load Data file into copy_paste storage
        try:
            file_open= open('Project_ADAM\STORAGE\copy_paste_storage_basic_programming.dat', 'rb')
            self.copy_paste_storage = pickle.load(file_open)
            file_open.close()
        except:
            print("excepted")
            self.copy_paste_storage = {}
        
        # gets self.
        try:
            self.b1 = self.copy_paste_storage['b1']
        except:
            print("Key Not Recognized")


        try:
            self.b2 = self.copy_paste_storage['b2']
        except:
            print("Key Not Recognized")
        
        try:
            self.b3 = self.copy_paste_storage['b3']
        except:
            print("Key Not Recognized")

        
        try:
            self.b4 = self.copy_paste_storage['b4']
        except:
            print("Key Not Recognized")

        

        ###### buttons
        self.for_loop_example = tkinter.Button(self.button_frame_left2,text="Copy: for loop example", command= lambda: self.action_button1(self.b1))
        self.for_loop_explanation = tkinter.Button(self.button_frame_left2, text="View Explanation")
        self.while_loop_example = tkinter.Button(self.button_frame_left2, text="Copy: while loop example", command= lambda: self.action_button1(self.b2))
        self.while_loop_explanation = tkinter.Button(self.button_frame_left2, text="Copy: while loop", command= lambda: self.action_button1(self.b2))
        self.open_dictionary_example = tkinter.Button(self.button_frame_left2, text="Copy: open a dictionionary from a dat file example", command= lambda:self.action_button1(self.b3))
        self.save_dictionary_to_dat = tkinter.Button(self.button_frame_left2, text="Copy: save a dictionary to a dat file function", command= lambda:self.action_button1(self.b4))
        
        self.open_data_input_entry_window = tkinter.Button(self.data_entry_frame1, text='Open data window', command= lambda: self.data_window_classes1())
        ###### BUTTONS ######


        self.label_assist_setting1.pack()
        self.for_loop_example.pack()
        self.for_loop_explanation.pack(side='left')
        self.while_loop_example.pack()
        self.while_loop_explanation.pack(side='left')
        self.open_dictionary_example.pack()
        self.save_dictionary_to_dat.pack()
        self.open_data_input_entry_window.pack(side='bottom')
        
        self.assist_basic_frame.pack(side='top')
        self.button_frame_left2.pack(side='left')
        self.data_entry_frame1.pack(side='bottom')
        


        

        

                    ################################################################


    def action_button1(self, text_placeholder):
        
        pyperclip.copy(text_placeholder)
        self.assistance_label2.set("Action has been Preformed")


    def data_window_classes1(self):

        try:
            input_file = open('Project_ADAM\STORAGE\copy_paste_storage_basic_programming.dat', 'r+b')
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
        self.convert_data_button = tkinter.Button(self.__data_frame, text="convert text to dictionary and append to dat file", command= lambda: self.append_data_to_file1())

                
            
                

        self.data_label.pack()
        self.data_key_entry.pack()
        self.data_entry_box.pack()
        self.convert_data_button.pack()
                
        self.__data_frame.pack()
    

    def append_data_to_file1(self):
        self.__data_key = self.data_key_entry.get()
        self.original_DATA_entry = self.data_entry_box.get("1.0", tkinter.END)
        
        try:
            call_name = self.__data_key
            code = self.original_DATA_entry
            self.copy_paste_storage[call_name] = code
            save_to_file = open('Project_ADAM\STORAGE\copy_paste_storage_basic_programming.dat', "r+b")
            pickle.dump(self.copy_paste_storage, save_to_file)
            save_to_file.close()
        except FileNotFoundError:
            save_to_file = open('Project_ADAM\STORAGE\copy_paste_storage_basic_programming.dat', "wb")
            pickle.dump(self.copy_paste_storage, save_to_file)
            save_to_file.close()

        print('action preformed')