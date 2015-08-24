from Tkinter import *
import Tkinter as tk

root = Tk()

value_out = StringVar()    
window = tk.Entry(root, textvariable = value_out, width=10)
window.grid(row=0)

def action():
    window.insert(END,'Clicked')



b = tk.Button(root,text='Click', command=action)
b.grid(row=1,sticky=(E,W))

root.mainloop()