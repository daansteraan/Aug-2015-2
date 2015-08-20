from Tkinter import *
import Tkinter as tk

# main window
root = Tk()
root.title('Calculator')

# button set
buttons = ['1','2','3','4','5','6','7','8','9','0','+','-','/','*','.']

# calculator sum value
sum_value = StringVar()
input_value = StringVar()        

def calc(x):   
    sum_value.set(x)
    return sum_value
    
# output window
output_window = tk.Label(root, textvariable=sum_value, width=20, height=2).grid(row=0, columnspan=3, sticky=(E,W))

# button creation
r=1
c=0

for i in buttons:
    if c < 2:
        tk.Button(root, text = i, command = calc(i), padx = 5, pady = 3).grid(row = r, column = c, sticky = (N,S,E,W))        
        c += 1
    else:
        tk.Button(root, text = i, command = calc(i), padx = 5, pady = 3).grid(row = r,column = c,sticky = (N,S,E,W))
        r  += 1
        c = 0
        
# clear and equals button
clear = tk.Button(root,text='=',padx = 5, pady=3).grid(row=6,column=0,sticky=(N,S,E,W))
clear = tk.Button(root,text='CLEAR',padx = 5, pady=3).grid(row=6,column=1, columnspan = 2,sticky=(N,S,E,W))

root.mainloop()
    