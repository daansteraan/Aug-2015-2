'''Find Cost of Tile to Cover W x H Floor - 

Calculate the total cost of tile it would take to cover a floor plan 
of width and height, using a cost entered by the user.'''

import math

print
print '*** TILE COST CALCULATOR ***'

print
width = raw_input('Enter room WIDTH(m): ')
length = raw_input('Enter room LENGTH(m): ')
room_area = round(float(width) * float(length),2)
print
print 'Room: %s X %s' % (width, length)
print 'Room Area: %.2f square meters' % room_area

print
tile_width = raw_input('Enter tile WIDTH(m): ')
tile_length = raw_input('Enter tile LENGTH(m): ')
tile_area = round(float(tile_width) * float(tile_length),2)
print
print 'Tile: %s X %s' % (tile_width, tile_length)
print 'Tile Area: %.2f square meters' % tile_area

print
tile_cost = float(raw_input('Enter tile cost : R '))
labour_cost = float(raw_input('Enter labour cost : R '))
print '------------------------------'

print
print 'RESULTS:'
print

tiles_required = math.ceil(room_area / tile_area)
total_cost = tiles_required * tile_cost + labour_cost

print 'Tiles required: %d' % int(tiles_required)
print 'Total cost: R %.2f'% total_cost

