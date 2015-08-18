a = 0
b = 1

def fib():    
    global a,b
       
    
    i = raw_input('how many terms? ')
    
    for j in range(int(i)):
        a,b = b,a  
        b += a
        yield a
             
for a in fib():
    print a,
