from Tkinter import *
import Tkinter as tk

root = Tk()

value_out = StringVar()
number = 0

def add_one():
    global number
    
    number += 1
    value_out.set(str(number))    
    
    
tk.Label(root, textvariable = value_out, height=2, width=10).grid(row=0)

b = tk.Button(root,text='click', command=add_one).grid(row=1,sticky=(E,W))


root.mainloop()