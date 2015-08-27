''' tkinter alarm clock'''

from Tkinter import *
import Tkinter as tk
import time
import winsound

alarm_clock = Tk()
alarm_clock.title('Alarm Clock')
alarm_clock.iconbitmap('favicon.ico')
alarm_clock.resizable(width=FALSE,height=FALSE)

current_time = ''

timer = tk.Label(alarm_clock,text=current_time)
timer.grid(row=0,column=1,pady=5, padx=20,columnspan=3)
time_label = tk.Label(alarm_clock, text = 'TIME :').grid(row=0,column=0)        

def updater():
    new_time = time.strftime("%H    |      %M     |     %S")
    timer.config(text=new_time)
    alarm_clock.after(100,updater)
    
alarm_time = tk.Label(alarm_clock, text = 'Alarm Time : ').grid(row=2,column=0, padx= 5,pady=5)

def set_alarm():     
    global alarm_check
    time_now = time.strftime('%H:%M%S')
    test.config(text='ACTIVATED')   
    
    h = int(time_now[0:2])    
    m = int(time_now[3:5])    
    s = int(time_now[5:])
    
    if (h==hour) and (m==minute) and (s==second):
        print 'SOUND THE ALARM'
        for i in range(20):
            winsound.Beep(1000,500)
    
    alarm_check = alarm_clock.after(10,set_alarm)
    
def reset():
    global hour, minute, second
    
    hour = 0
    minute = 0
    second = 0
    
    hours.config(text='0'+str(hour%24))
    minutes.config(text='0'+str(minute%60))
    seconds.config(text='0'+str(second%60))
    
    test.config(text='SET ALARM')    
    
    try:
        alarm_clock.after_cancel(alarm_check)
    except:
        pass
    
test = tk.Button(alarm_clock, text='SET ALARM', command=set_alarm)
test.grid(row=3,column=1,columnspan=3,sticky=(E,W))
clear = tk.Button(alarm_clock, text='RESET', command=reset)
clear.grid(row=3,column=0,sticky=(E,W))

        
# alarm functions
hour = 0
minute = 0
second = 0

def hour_increment():
    global hour
    hour += 1
    if hour%24 < 10:
        hours.config(text='0'+str(hour%24)) 
    else:
        hours.config(text=hour%24)
        
def minute_increment():
    global minute
    minute += 1
    if minute%60 < 10:
        minutes.config(text='0'+str(minute%60))    
    else:
        minutes.config(text=minute%60)
        
def second_increment():
    global second
    second += 1
    if second%60 < 10:
        seconds.config(text='0'+str(second%60))
    else:
        seconds.config(text=second%60)
    
#alarm buttons
hours = tk.Button(alarm_clock, text=hour, command = hour_increment)
hours.grid(row=2,column=1,sticky=(E,W))
minutes = tk.Button(alarm_clock, text=minute, command = minute_increment)
minutes.grid(row=2,column=2,sticky=(E,W))
seconds = tk.Button(alarm_clock, text=second, command = second_increment)
seconds.grid(row=2,column=3,sticky=(E,W))

reset()
updater() 
alarm_clock.mainloop()