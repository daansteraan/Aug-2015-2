''' Some Tkinter event loops'''

from Tkinter import *
import Tkinter as tkinter

root = Tk()
root.title('event window')

frame = tkinter.Frame(root, relief='ridge', borderwidth=50).grid(row=2,column=2,sticky=(N,S,E,W))

label_1 = tkinter.Label(frame, text='waiting...', padx=200,pady=200)

label_1.pack(fill='both')
label_1.bind('<Enter>', lambda event: label_1.configure(text='pointer entered window'))
label_1.bind('<Leave>', lambda event: label_1.configure(text='pointer left window'))
label_1.bind('<1>', lambda event: label_1.configure(text='left clicked at %d,%d' % (event.x, event.y)))
label_1.bind('<3>', lambda event: label_1.configure(text='right clicked at %d,%d' % (event.x, event.y)))


root.mainloop()