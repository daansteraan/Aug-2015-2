''' techwak.weebly.com - calculator tutorial '''

from Tkinter import *
import Tkinter as tk
import tkMessageBox

calculator = Tk()

calculator.title('Calculator')
calculator.geometry('248x142')

screen = tk.Frame(calculator, width=500, height=500, relief='sunken')
buttons = tk.Frame(calculator, width=5,height=1, relief='groove')
screen.grid(column=0,row=0,columnspan=5,sticky=(E,W))
buttons.grid(column=0,row=1,padx=1)

numbers=StringVar()
results = tk.Entry(screen, textvariable=numbers, width=24)
results.pack # hope that doesn't stuff things up
results.grid(row=0,column=0,sticky=(E,W)) 
menubar = Menu(calculator)

def appear(x):
    return lambda: results.insert(END,x)
        
def zero():
    results.insert(END,'0')
    
def refresh():
    results.insert(0,END)

def equals():
    try:
        result = eval(results.get())
    except:
        result='Invalid Sum'
        
    results.delete(0,END)
    results.insert(0,result)

def dot():
    results.insert(END,'.')

def bracket_1():
    results.insert(END,'(')        

def bracket_2():
    results.insert(END,')')

def product():
    results.insert(END,'*')                        

def divide():
    results.insert(END,'/')        

def plus():
    results.insert(END,'+')        

def minus():
    results.insert(END,'-')
    
def delete():
    results.delete(-1)    

# Menubar - I omit the scientific bit
def quit1():
    if tkMessageBox.askokcancel("Quit","Are you sure you want to quit?"):
        calculator.destroy()
        
viewMenu = Menu(menubar, tearoff = 1)
viewMenu.add_command(label='Quit', command = quit1)
menubar.add_cascade(label="View", menu=viewMenu)

# number buttons
nums = ['7','4','1','8','5','2','9','6','3']
for index in range(9):
    n=nums[index]
    tk.Button(buttons, text=n,width=5,height=1, command=appear(n)).grid(padx=2,pady=2,row=index%3,column=index/3)
    
#fuction buttons:
delete_b = tk.Button(buttons,text='del',width=5,height=1, command=delete)
delete_b.grid(padx=2, pady=2, column=3, row=0)

product_b = tk.Button(buttons,text='*',width=5,height=1, command=product)
product_b.grid(padx=2, pady=2, column=3, row=1)

divide_b= tk.Button(buttons,text='/',width=5,height=1, command=divide)
divide_b.grid(padx=2, pady=2, column=4, row=1)

plus_b= tk.Button(buttons,text='+',width=5,height=1, command=plus)
plus_b.grid(padx=2, pady=2, column=3, row=2)

minus_b= tk.Button(buttons,text='-',width=5,height=1, command=minus)
minus_b.grid(padx=2, pady=2, column=4, row=2)

brack_1 = tk.Button(buttons,text='(',width=5,height=1, command=bracket_1)
brack_1.grid(padx=2, pady=2, column=2, row=3)

brack_2= tk.Button(buttons,text=')',width=5,height=1, command=bracket_2)
brack_2.grid(padx=2, pady=2, column=3, row=3)

zero_b= tk.Button(buttons,text='0',width=5,height=1, command=zero)
zero_b.grid(padx=2, pady=2, column=0, row=3)

refresh_b= tk.Button(buttons,text='C',width=5,height=1, command=refresh)
refresh_b.grid(padx=2, pady=2, column=4, row=0)

dot_b= tk.Button(buttons,text='.',width=5,height=1, command=dot)
dot_b.grid(padx=2, pady=2, column=1, row=3)

equals_b= tk.Button(buttons,text='=',width=5,height=1, command=equals)
equals_b.grid(padx=2, pady=2, column=4, row=3)


calculator.config(menu=menubar)
calculator.mainloop()