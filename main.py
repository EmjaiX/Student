import tkinter as tk
from functools import partial

class emjaibutton:

    color = [["black","white"],["red","grey"],["orange","blue"],["red","green"],["teal","black"],["tan","indigo"]]
    def __init__(self,root):
        self.root = tk.Frame(root)
        self.root.pack()

        for i in range(6):
            self.button = tk.Button(self.root, text = str("Button "+ str(i)),fg=self.color[i][0],bg=self.color[i][1])
            
            self.button.bind("<Button-1>",self.leftClick)
            self.button.bind("<Button-3>",self.rightClick)
            self.button.pack()
        
        self.label = tk.Label(self.root,text="lorem ipsum" , bg="purple",fg="orange")
        self.label.pack()

    def leftClick(self,event):
        self.item = event.widget
        print (self.item.cget('bg'))
        print("left click")
        
    def rightClick(self,event):
        print("right click")

        


root = tk.Tk()

root.title("Homework 2")
eb = emjaibutton(root)
root.mainloop()
