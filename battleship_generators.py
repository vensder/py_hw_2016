#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

dimensions = 10 # dimensions of the field

# generating area dim x dim (10 x 10)
area = [[0 for i in range(dimensions)] for i in range(dimensions)]

# Count quantity of random generation x,y
iterations = 0

def print_area(area):
    ''''Print battle field matrix with vertical coordinates'''
    for count, row in enumerate(area,1):
        print('%2d' % (count), (' '.join(row)), '%1d' % (count))

def transpon_matrix(matrix):
    '''Transpose the matrix via generator expression'''
    return [[matrix[i][j] for i in range(dimensions)] for j in range(dimensions)]

def transpon_random(matrix):
    '''Call the transpon_matrix() with 50% of probability'''
    if randint(0,1):
        return transpon_matrix(matrix)
    else:
        return matrix

def generate_xy(decks_number):
    '''Generate x,y coordinates for ship with decks = decks_number'''
    x = randint(0, dimensions - decks_number)
    y = randint(0, dimensions - 1)
    # Count quantity of random generation x,y
    global iterations
    iterations += 1
    return(x,y)
    
def insert_horizontal(decks_number):
    '''Insert horizontal ship in x,y, if there is 0'''
    x,y = generate_xy(decks_number)
    # Regenerate x,y while we would not find the free area for ship
    while sum(area[y][x:x+decks_number]) != 0:
        x,y = generate_xy(decks_number)
    
    # Insert row with '2' above ship, if it is not first row
    if y > 0:
        area[y-1][x:x+decks_number] = [2 for i in range(decks_number)]
        # Insert '2' in left and right side above ship
        if x > 0:
            area[y-1][x-1] = 2
        if x < (dimensions - decks_number):
            area[y-1][x+decks_number] = 2
    
    # Insert ship with '1'
    area[y][x:x+decks_number] = [1 for i in range(decks_number)]
    
    # Insert '2' with left and right side of the ship
    if x > 0:
        area[y][x-1] = 2
    if x < (dimensions - decks_number):
        area[y][x+decks_number] = 2
    
    # Insert row with '2' below ship, if it is not last row
    if y < (dimensions - 1):
        area[y+1][x:x+decks_number] = [2 for i in range(decks_number)]
        # Insert '2' in left and right side below ship
        if x > 0:
            area[y+1][x-1] = 2
        if x < (dimensions - decks_number-1):
            area[y+1][x+decks_number] = 2

def convert_to_ascii(area): # use generator expression
    '''Convert field with 0,1,2 to ascii (---xxx--)'''
    return [['x' if area[i][j] == 1 else '-' for i in range(dimensions)] for j in range(dimensions)]

# insert ship with 4 decks
insert_horizontal(4)

# transponse matrix random befor insert each 2 ship with 3 decks
for i in range(2):
    area = transpon_random(area)
    insert_horizontal(3)

# transponse matrix random befor insert each 3 ship with 2 decks
for i in range(3):
    area = transpon_random(area)
    insert_horizontal(2)

# insert 4 ship with 1 deck
for i in range(4):
    insert_horizontal(1)

# horizontal coordinates
print('   a b c d e f g h i j')
#print('   ___________________')
# convert to ascii (area)
print_area(convert_to_ascii(area))
print('   a b c d e f g h i j')

print('\n-------------------\n')
print(u'Iterations: ', iterations)

# programms and opponents shots store in the sets of tuples: {(x,y)}
# each next shot write to the file (rewrite file with coord x,y)
# another ex. of app rereads the file (opened with reading). If coords changed, read it and store,
# and write own shot to own file (opened with rewriting)
