''' tkinter alarm clock'''

from Tkinter import *
import Tkinter as tk
import datetime
import time

alarmclock = Tk()
alarmclock.title('Alarm Clock')


current_time = time.ctime()

def updater():
    new_time = time.ctime()
    if new_time != current_time:
        timer.config(text=new_time)

timer = tk.Label(alarmclock,text=current_time,width=30)
timer.grid(row=0,column=0,pady=5)

update_time = tk.Button(alarmclock, text='Update', command = updater)
update_time.grid(row=1,pady=5,sticky=(E,W))
  
alarmclock.after(1000,updater)  
  
alarmclock.mainloop()