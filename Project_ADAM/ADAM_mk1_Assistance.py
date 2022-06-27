# foundation for future ADAM integrations
# these parts will be a mix between ADAM_GUI and ADAM MAIN, 
# these sections will either replace the standard welcome text with displayed information, or could possibly open up more TKinter windows,
# it depends on what the user needs help with
import tkinter

class Assist_Module_MK1:
    


    def open_assistance_window(self):
        self.top_assitance = tkinter.Toplevel()

        self.test_frame = tkinter.Frame(self.top_assitance)


        self.assistance_label= tkinter.StringVar()

        self.assistance_label.set("What would you like assistance with?")

        self.label_assist_speak = tkinter.Label(self.test_frame, textvariable = self.assistance_label)  

        self.entry_box_assist = tkinter.Entry(self.test_frame)

        self.search = tkinter.Button(self.test_frame, text="Search", command = self.ADAM_ASSIST_V1)






        self.label_assist_speak.pack()
        self.__entry_box.pack()
        self.search.pack()
        
        self.test_frame.pack()


    def ADAM_ASSIST_V1(self):

        print("passed into")

        self.user_entry_assist = str(self.entry_box_assist.get())
        

       
        
        # for every item in the test list, do an action
        
        if "AI" in self.user_entry_assist:
            print("AI")
            
    
        if "i eat?" in self.user_entry_assist:
            print("I eat?")
                
           
        

    


