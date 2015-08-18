from Tkinter import *
import Tkinter as tkinter

root = Tk()

root.title('Feet / Meters converter')

# function
def calculate_ftm(*args):
    
    try:
        value_1 = float(feet_in.get())
        meters_out.set((0.3048 * value_1 * 10000.0 + 0.5)/10000.0)
    except:
        pass
    
def calculate_mtf(*args):
    
    try:
        value_2 = float(meters_in.get())
        feet_out.set((value_2*10000-0.5)/3048)
    except:
        pass
    
# Frame
mainframe = tkinter.Frame(root, padx=12, pady=12)
mainframe.grid(column=0,row=0, sticky=(N,S,E,W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Entry in feet
feet_in = StringVar()
meters_out = StringVar()

feet_out = StringVar()
meters_in = StringVar()

feet_entry = tkinter.Entry(mainframe, textvariable=feet_in)
feet_entry.grid(column=2,row=1, sticky=(W,E))

meters_entry = tkinter.Entry(mainframe, textvariable=meters_in)
meters_entry.grid(column=2,row=4, sticky=(W,E))

# labels
tkinter.Label(mainframe,textvariable=meters_out).grid(row=2,column=2,sticky=(W,E))
tkinter.Label(mainframe,text='feet').grid(column=3,row=1,sticky=W)
tkinter.Label(mainframe,text='is equivalent to').grid(column=1,row=2,sticky=E)
tkinter.Label(mainframe,text='meters').grid(column=3,row=2,sticky=W)

tkinter.Label(mainframe,textvariable=feet_out).grid(row=5,column=2,sticky=(W,E))
tkinter.Label(mainframe,text='meters').grid(column=3,row=4,sticky=W)
tkinter.Label(mainframe,text='is equivalent to').grid(column=1,row=5,sticky=E)
tkinter.Label(mainframe,text='feet').grid(column=3,row=5,sticky=W)

# button
tkinter.Button(mainframe, text='Calculate', command=calculate_ftm).grid(column=3,row=3,sticky=W)
tkinter.Button(mainframe, text='Calculate', command=calculate_mtf).grid(column=3,row=6,sticky=W)

# decor
for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)
    
feet_entry.focus()

# startup
root.mainloop()
