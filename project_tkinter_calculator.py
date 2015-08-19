from Tkinter import *
import Tkinter as tk

root = Tk()

buttons = ['1','2','3','4','5','6','7','8','9','0','+','-','/','*','=']
row = 1
column = 1

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky=(N,S,E,W))
frame.rowconfigure(0,weight=1)
frame.columnconfigure(0,weight=1)


calc_window = StringVar()
window = tk.Label(root, textvariable=calc_window)
window.pack(side='top')

for i in buttons:
    if row < 3:
        tk.Button(frame,text=i).grid(row=row,column=column)
        row += 1
        column += 1
    else:
        row = 1
        column = 1
        
root.mainloop()
    