import tkinter as tk
from functools import partial

class emjaibutton:

    def __init__(self,root):
        self.root = tk.Frame(root)
        self.root.grid()

        self.button = tk.Button(self.root, text = "The only button")
        
        self.button.bind("<Button-1>",self.leftClick)
        self.button.bind("<Button-3>",self.rightClick)
        self.button.grid()

    def leftClick(self,event):
        print("left click")
        
    def rightClick(self,event):
        print("right click")

        


root = tk.Tk()

root.title("Homework 2")
eb = emjaibutton(root)
root.mainloop()
