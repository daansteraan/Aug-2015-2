"""
Next Prime Number - Have the program find prime numbers until the user chooses 
to stop asking for the next one.

"""

print 
print "*** PRIME NUMBERS ***"

prime_list = []
      
for i in range(2,1000):     
    for j in range(2,1000):
        if i % j == 0:              
            if (i == j):                     
                prime_list.append(i)
            break            
        else:            
            pass

print
print 'Press ENTER for the next prime number'

for k in prime_list:   
    prompt = raw_input('')  
    if prompt == '':
        print k,                  
    else:
        break
    
        