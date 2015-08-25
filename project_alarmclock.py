''' tkinter alarm clock'''

from Tkinter import *
import Tkinter as tk
import datetime
import time

alarmclock = Tk()
alarmclock.title('Alarm Clock')

time_1 = StringVar()

timer = tk.Label(alarmclock,width=30)
timer.grid(row=0,column=0,pady=5)

time_2 = time.ctime()

while True:
    if time_1 != time_2:
        time_1 = time_2        
        timer.config(text=time_1)
        alarmclock.update_idletasks()
        time.sleep(1)
  
alarmclock.mainloop()