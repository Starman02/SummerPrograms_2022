
import tkinter

from pkg_resources import set_extraction_path




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



#####PASS OFF ENGINE##############



    def set_entry_brain(self):
        user_entry = str(self.entry_box.get())
        print("passed into")
        print(user_entry)
        
        

        if user_entry == "decision help":
            print("need assistance?")

           

        








############################################################################################################################################################################################################################################################################################################################


"""
Main running class for adam

"""





# class ADAM_V1: 
    

#     def __init__(self, command_ADAM):
#         self.command_adam = command_ADAM





#     def set_entry_brain(self, command_adam):
#         print("passed into")
#         print(command_adam)
        
        
#         self.main_storage = command_adam

#         if self.main_storage == "decision help":
#             print("need assistance?")

           



start_ADAM = ADAM_GUI_V1()




