''' tkinter calculator '''

import Tkinter as tkinter
from Tkinter import Tk

# main window
window = Tk()
window.geometry('260x50')

# number buttons
for i in range(10):
    button_i = tkinter.Button(window,text=i)
    button_i.pack(side='left')

# operator buttons
button_m = tkinter.Button(window,text='*')
button_m.pack(side='left')

button_d = tkinter.Button(window,text='/')
button_d.pack(side='left')

button_a = tkinter.Button(window,text='+')
button_a.pack(side='left')

button_s = tkinter.Button(window,text='-')
button_s.pack(side='left')

button_e = tkinter.Button(window,text='=')
button_e.pack(side='left')

window.mainloop()