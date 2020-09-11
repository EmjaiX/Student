import tkinter as tk
from functools import partial

class emjaibutton:

    color = [["black","white"],["red","grey"],["orange","blue"],["red","green"],["teal","black"],["tan","indigo"]]
    def __init__(self,root):
        self.root = tk.Frame(root)
        self.root.pack()

        self.start = 2
        self.cspan = 4
        self.rspan = 2
        self.padding = 5
        self.row =  self.start
        self.column = self.start
        self.count = 0
        for i in range(6):
            self.button = tk.Button(self.root, text = str("Button "+ str(i)),fg=self.color[i][0],bg=self.color[i][1])
            
            self.button.bind("<Button-1>",self.leftClick)
            self.button.bind("<Button-3>",self.rightClick)
            self.button.grid(row = self.row, column = self.column, columnspan = self.cspan, rowspan = self.rspan, pady = self.padding, padx = self.padding)
            self.column += self.padding
            self.count += 1
            if (self.count%5==0):
                self.row += self.padding
                self.column = self.start
        
        self.label = tk.Label(self.root,text="lorem ipsum" , bg="purple",fg="orange")
        self.label.grid(row = self.row, column = self.column + 5 * self.count, columnspan = 3, rowspan = 2, pady = (20, 5), padx = 5)

    def leftClick(self,event):
        self.item = event.widget
        self.label.config(bg=self.item.cget('bg'))
        
    def rightClick(self,event):
        self.item = event.widget
        self.label.config(fg=self.item.cget('fg'))

        


root = tk.Tk()

root.title("Homework 2")
eb = emjaibutton(root)
root.mainloop()
