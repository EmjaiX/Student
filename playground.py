from tkinter import *
from tkinter import messagebox
root = Tk()

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\chapelle.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
root.mainloop()