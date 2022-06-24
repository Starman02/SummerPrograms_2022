
import json
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
        user_entry = str(self.entry_box.get())
        updated_search = user_entry.replace(" ", "_")

        with open('D:\Summer_Programs_2021\Project_ADAM\ADAM_AI_STORAGE\ADAM_SEARCH_ENGINE.txt', 'r') as filehandle:
            ADAM_SEARCH_QUERIES = json.load(filehandle)
        


        

        
        # for every item in the test list, do an action
        for i in ADAM_SEARCH_QUERIES:
            print(i)
            if updated_search == i:
                print("WHOOOOP")
        

        


        print("passed into")
        print(updated_search) 
        
        

        if user_entry == "decision help":
            print("need assistance?")

           

        








############################################################################################################################################################################################################################################################################################################################


start_ADAM = ADAM_GUI_V1()

