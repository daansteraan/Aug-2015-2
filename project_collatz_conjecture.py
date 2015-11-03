'''Collatz Conjecture - Start with a number n > 1. 
Find the number of steps it takes to reach one using 
the following process: If n is even, divide it by 2. 
If n is odd, multiply it by 3 and add 1.'''

number = int(raw_input('enter number: '))
count = 0

while number != 1:
    if number % 2 == 0:
        number /= 2
        count += 1
        print number
    elif number % 2 == 1:
        number = (number*3) + 1
        count += 1
        print number
        
print 'COUNT: ', count
        
        