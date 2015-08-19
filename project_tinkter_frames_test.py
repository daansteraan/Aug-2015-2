from Tkinter import *
import Tkinter as tk

root = Tk()

frame_1 = tk.Frame(root,relief='ridge')
frame_1.grid(row=1,column=1)
frame_1.rowconfigure(0,weight=4)
frame_1.columnconfigure(0,weight=4)

tk.Label(frame_1, text="row 1 column 1", relief='sunken',bg='red',padx=10,pady=10).grid(row=1,column=1)
tk.Label(frame_1, text="row 1 column 2", relief='ridge',bg='pink',padx=10,pady=10).grid(row=1,column=2)
tk.Label(frame_1, text="row 2 column 1", relief='groove',bg='green',padx=10,pady=10).grid(row=2,column=1)
tk.Label(frame_1, text="row 2 column 2", relief='ridge',bg='yellow',padx=10,pady=10).grid(row=2,column=2)

root.mainloop()