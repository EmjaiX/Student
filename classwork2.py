import tkinter as tk
from functools import partial
from support import *

def showFace(face):
    print("hello")
    global wid
    global mes
    if face=="J":
        buzz = "Have a Coke and stay up."
    elif face=="K":
        buzz = "Take a stretch caz` you're."
    elif face=="L":
        buzz = "It's gonna be okay!."
    mes.config(text=buzz)
    wid.config(text=face)
# class Lexan:
#     def Lexan():
#     def __init__(self):
root = tk.Tk()
wid = tk.Label(root,text="How are you feeling today?",fg="orange",font=(64))
wid.grid(row=2,column=2,columnspan=2,rowspan=2,padx=2,pady=10)

wid = tk.Button(root,text="Happy",command=partial(showFace,"J"))
wid.grid(row=8,column=2,columnspan=1,rowspan=2,pady=10)

wid = tk.Button(root,text="Okay",command=partial(showFace,"K"))
wid.grid(row=8,column=3,columnspan=1,rowspan=2,pady=10)

wid = tk.Button(root,text="Sad",command=partial(showFace,"L"))
wid.grid(row=8,column=4,columnspan=1,rowspan=2,padx=(0,10),pady=10)


wid = tk.Label(root,text="a",font=("Wingdings", 64))
wid.grid(row=4,column=2,columnspan=2,rowspan=2,padx=2,pady=10)

mes = tk.Label(root,text="",fg=GenerateHexColor(),font=( 64))
mes.grid(row=6,column=2,columnspan=2,rowspan=2,padx=2,pady=10)

root.mainloop()