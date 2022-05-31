import tkinter as tk
from tkinter import ttk
from tkinter import * 


root = Tk()

# This is the section of code which creates the main window
root.geometry('810x530')
root.configure(background='#9ACD32')
root.title('Hello, I\'m the main window')


# First, we create a canvas to put the picture on
jumanji= Canvas(root, height=810, width=530)
# Then, we actually create the image file to use (it has to be a *.gif)
picture_file = PhotoImage(file = 'Doominiser_Eternal\senorDoomington.png')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
jumanji.create_image(810, 0, anchor=NE, image=picture_file)
jumanji.place(x=-1, y=0)


# This is the section of code which creates the a label
Label(root, text='oh yeahhhhhh', bg='#9ACD32', font=('arial', 12, 'normal')).place(x=99, y=70)


root.mainloop()
