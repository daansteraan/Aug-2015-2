'''Fibonacci Sequence - Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number.'''

import time

print
print "*** FIBONACCI SEQUENCES ***"

fib_list = [0,1]

terms = int(raw_input('please input the number of terms: ')) 
    
for i in range(terms):
    
    
    new_value = fib_list[-1] + fib_list[-2]
    fib_list.append(new_value)

print    
print "SEQUENCE :", 

for i in fib_list[:terms]:
    print i,
    time.sleep(0.5)


