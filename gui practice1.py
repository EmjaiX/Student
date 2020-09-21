import tkinter as tk
from functools import partial

root = tk.Tk()

items = ["Banana Bread","Peanut Slush","Papaya Cake"]
prices = [3.5,2.75,4.5]
tax = 1.0
total = 0.0
cartq = [0,0,0]
def addItem(item_no):
    cartq[item_no - 1] += 1
def checkout():
    sub_root = tk.Tk()
    i = 0
    has_Item = False
    for item in items:
        if(cartq[i] >0):
            has_Item = True
            line = item + "   qty " + str(cartq[i]) + "   $"  + str(cartq[i] *prices[i])
            global total 
            total += cartq[i] *prices[i]
            l = tk.Label(sub_root, text=line, bg="black", fg="white" )
            l.pack(padx=5, pady=10, side=tk.TOP)
        i += 1
    line = "  Sub-Total  $" + str(total)  
    l = tk.Label(sub_root, text=line, bg="black", fg="white" )
    l.pack(padx=5, pady=10, side=tk.TOP)
    line = "  Total  $" + str(total*tax)    
    l = tk.Label(sub_root, text=line, bg="black", fg="white" )
    l.pack(padx=5, pady=10, side=tk.TOP)
    if(has_Item):
        tk.mainloop()


w = tk.Button(root, text="Banana Bread", bg="red", fg="white" ,command=lambda: addItem(1))
# w.pack(padx=5, pady=10, side=tk.LEFT)
w.grid(row = 1, column = 1, columnspan = 4, rowspan = 2, pady = 5, padx = 5)
w = tk.Button(root, text="Peanut Slush", bg="green", fg="black",command=partial(addItem,2))
w.grid(row = 1, column = 6, columnspan = 4, rowspan = 2, pady = 5, padx = 5)
w = tk.Button(root, text="Papaya Cake", bg="blue", fg="white",command=partial(addItem,3))
# w.pack(padx=5, pady=20, side=tk.LEFT)
w.grid(row = 1, column = 11, columnspan = 3, rowspan = 2, pady = 5, padx = 5)
w = tk.Button(root, text="Check Out", bg="white", fg="purple",command=checkout)
w.grid(row = 7, column = 11, columnspan = 3, rowspan = 2, pady = (20, 5), padx = 5)
tk.mainloop()