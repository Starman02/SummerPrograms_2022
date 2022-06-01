
from tkinter import *
from PIL import ImageTk, Image


root = Tk()

canv = Canvas(root, width=800, height=900, bg='white')
canv.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open("D:\Summer_Programs_2021\SummerPrograms_2022\Doominiser_Eternal\senorDoomington.png"))  # PIL solution
canv.create_image(500, 500, anchor=NW, image=img)

mainloop()
