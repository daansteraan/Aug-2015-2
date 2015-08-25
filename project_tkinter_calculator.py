''' What i really like about this project is that is really is simple. 
the whole thing can easily be shortened to less than 50 lines of code and
still work perfectly, which was the initial objective. '''

from __future__ import division
from Tkinter import *
import Tkinter as tk
import tkMessageBox

# main window
root = Tk()
root.title('Calculator')

# button set
buttons = ['1','2','3','4','5','6','7','8','9','0','+','-','/','*','.']

sum_value = StringVar()

def main_window(x):
    return lambda: output_window.insert(END,x)
   
# output window
output_window = tk.Entry(root, textvariable=sum_value, width=25, font = 'courier 10')
output_window.grid(row=0, columnspan=3, sticky=(E,W))

def equals():
    try:
        result = eval(output_window.get())
    except:
        result = 'INVALID'
    
    output_window.delete(0,END)
    output_window.insert(0,result)

def refresh():
    output_window.delete(0,END)
    
# button creation
r=1
c=0

for i in buttons:
    if c < 2:
        tk.Button(root, text = i, command = main_window(i), pady = 3).grid(row = r, column = c, sticky = (N,S,E,W))        
        c += 1
    else:
        tk.Button(root, text = i, command = main_window(i), pady = 3).grid(row = r,column = c,sticky = (N,S,E,W))
        r  += 1
        c = 0
        
# clear and equal button
equal = tk.Button(root,text='=',padx = 5, pady=3, command=equals)
equal.grid(row=6,column=0,sticky=(N,S,E,W))

clear = tk.Button(root,text='CLEAR',padx = 5, pady=3,command = refresh)
clear.grid(row=6,column=1, columnspan = 2,sticky=(N,S,E,W))

#menu
menubar = Menu(root)

def quit1():
    if tkMessageBox.askokcancel("Quit","Are you sure you want to quit?"):
        root.destroy()
        
viewMenu = Menu(menubar)
viewMenu.add_command(label='Quit', command = quit1)
menubar.add_cascade(label="Home", menu=viewMenu)


root.config(menu=menubar)
root.mainloop()
    