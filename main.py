import tkinter as tk
from functools import partial

class emjaibutton:

    color = [["black","white"],["red","grey"],["orange","blue"],["red","white"],["black","white"],["black","white"]]
    def __init__(self,root):
        self.root = tk.Frame(root)
        self.root.pack()

        for i in range(6):
            self.button = tk.Button(self.root, text = str("Button "+ str(i)))
            
            self.button.bind("<Button-1>",self.leftClick)
            self.button.bind("<Button-3>",self.rightClick)
            self.button.pack()
        
        self.label = tk.Label(self.root)

    def leftClick(self,event):
        print("left click")
        
    def rightClick(self,event):
        print("right click")

        


root = tk.Tk()

root.title("Homework 2")
eb = emjaibutton(root)
root.mainloop()
