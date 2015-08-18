"""

Change Return Program - The user enters a cost and then the amount of \
money given. The program will figure out the change and the number of \
quarters, dimes, nickels, pennies needed for the change.

"""

name = 'Change Return Calculator'
print
print name
print '-'* len(name)
print 

# inputs
item_cost = float(raw_input('Enter item price: R '))
cash = float(raw_input('Enter amount tendered: R '))

change = cash - item_cost
change = float(change)

print
print 'CHANGE: R %.2f' % change
print

# money variables

note_200 = 0
note_100 = 0
note_50 = 0
note_20 = 0
note_10 = 0

coin_5 = 0
coin_2 = 0
coin_1 = 0
coin_50c = 0
coin_20c = 0
coin_10c = 0
coin_5c = 0

while change >= 0.05:
    
    # R 200 notes    
    while change - 200 >= 0:                
        change -= 200
        note_200 += 1
            
    if note_200 > 0: 
        print 'R 200 notes: ', int(note_200)
    
    # R 100 notes    
    while change - 100 >= 0:                
        change -= 100
        note_100 += 1
    
    if note_100 > 0:        
        print 'R 100 notes: ', int(note_100)
    
    # R 50 notes    
    while change - 50 >= 0:                
        change -= 50
        note_50 += 1
            
    if note_50 > 0:        
        print 'R 50 notes: ', int(note_50)
    
    # R 20 notes    
    while change - 20 >= 0:                
        change -= 20
        note_20 += 1
    
    if note_20 > 0:        
        print 'R 20 notes: ', int(note_20)
    
    # R 10 notes    
    while change - 10 >= 0:                
        change -= 10
        note_10 += 1

    if note_10 > 0:            
        print 'R 10 notes: ', int(note_10)
    
    # R 5 coin    
    while change - 5 >= 0:                
        change -= 5
        coin_5 += 1
            
    if coin_5 > 0:
        print 'R 5 coins: ', int(coin_5)
    
    # R 2 coin    
    while change - 2 >= 0:                
        change -= 2
        coin_2 += 1
            
    if coin_2 > 0:
        print 'R 2 coins: ', int(coin_2)
    
    # R 1 coin    
    while change - 1.0 >= 0.0:                
        change -= 5
        coin_1 += 1
            
    if coin_1 > 0:
        print 'R 1 coins: ', int(coin_1)
    
    # 50 c coin    
    while float(change) - 0.5 >= 0.0:                
        change -= 0.5
        coin_50c += 1
            
    if coin_50c > 0:
        print '50c coins: ', int(coin_50c)
    
    # 20 c coin    
    while float(change) - 0.2 >= 0.0:                
        change -= 0.2
        coin_20c += 1
            
    if coin_20c > 0:
        print '20c coins: ', int(coin_20c)
    
    # 10 c coin    
    while change - 0.1 >= 0.0:                
        change -= 0.1
        coin_10c += 1
            
    if coin_10c > 0:
        print '10c coins: ', int(coin_10c)
    
    # 5 c coin    
    while change - 0.05 >= 0.0:                
        change -= 0.05
        coin_5c += 1
            
    if coin_5c > 0:
        print '5c coins: ', int(coin_5c)
    
    break
    


