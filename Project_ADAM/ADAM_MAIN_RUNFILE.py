
import json
from platform import win32_edition
import tkinter





class ADAM_GUI_V1:

    def __init__(self):
        self.main_window = tkinter.Tk()



        



        self.text_speaking_frame = tkinter.Frame(self.main_window)
        
        # this frame will have a entry box allowing the user to interact with ADAM and call specific commands
        self.entry_frame = tkinter.Frame(self.main_window)

        self.ADAM_LABEL = tkinter.StringVar()

        self.ADAM_LABEL.set("Welcome To ADAM Basic")

        
        

        self.label_speak = tkinter.Label(self.text_speaking_frame, textvariable = self.ADAM_LABEL)      # self.text will hold the welcome text as well as be the text for ADAM to talk back to you from
        self.ADAM_text_variable = str("")
        self.entry_box = tkinter.Entry(self.entry_frame)
        
        self.begin_search = tkinter.Button(self.entry_frame, text="Begin Search", command = self.set_entry_brain)


        self.label_speak.pack()
        self.entry_box.pack()
        self.begin_search.pack()


        self.text_speaking_frame.pack()
        self.entry_frame.pack()
        tkinter.mainloop()

    def get_entry_text(self):
        return self.ADAM_LABEL 



#######SEARCHENGINE#######################################################################################################################################################################################       



    def set_entry_brain(self):

        print("passed into")

        self.user_entry = str(self.entry_box.get())
        

        with open('D:\Summer_Programs_2021\Project_ADAM\ADAM_AI_STORAGE\ADAMSE_DECISION_V1.txt', 'r') as filehandle:
            ADAM_SEARCH_QUERIES_DECISION = json.load(filehandle)
        

        with open('D:\Summer_Programs_2021\Project_ADAM\ADAM_AI_STORAGE\ADAMSE_ASSISTANCE_V1.txt', 'r') as filehandle:
            ADAM_SEARCH_QUERIES_ASSISTANCE = json.load(filehandle)
        

        
        # for every item in the test list, do an action
        for d in ADAM_SEARCH_QUERIES_DECISION:
            if d in self.user_entry:
                print("DECIDING")
                break
        for a in ADAM_SEARCH_QUERIES_ASSISTANCE:
            if a in self.user_entry:
                print("AIDING")
                self.top_assitance = tkinter.Toplevel()

                self.test_frame = tkinter.Frame(self.top_assitance)
                self.test_label = tkinter.Label(self.test_frame, text="cheeseburger")
                self.test_label.pack()
                self.test_frame.pack()
                
                break
                
                
                
        

        


        
  
        
        

        

           

        








############################################################################################################################################################################################################################################################################################################################


start_ADAM = ADAM_GUI_V1()

