''' -> x coord ->
--------xx  y
-----       |
----xxxx--  v
----------
---x----xx
---x------
---x------
----------
xxx-------
----------
1234567890

[0,0,0,0,0,0,0,0,0,0]
'''

from random import randint

dimensions = 7 # dimensions of the field

# generating area dim x dim (10 x 10)
area = [[0 for i in range(dimensions)] for i in range(dimensions)]

# Count quantity of random generation x,y
iterations = 0

# Print battle field
def print_area(area):
    for r in area:
        print(' '.join(r))

# transpose the matrix
def transpon_matrix(matrix):
    matrix_t = [[0 for i in range(dimensions)] for i in range(dimensions)]
    for i in range(dimensions):
        for j in range(dimensions):
            matrix_t[i][j] = matrix[j][i]
    return matrix_t

#cells<N> = N
#ship<N>v = [1 for i in range(cells<N>)]

# call the transpon_matrix() with 50% of probability
def transpon_random(matrix):
    if randint(0,1) == 1:
        matrix = transpon_matrix(matrix)
        return matrix
    else:
        return matrix

# Generate x,y coordinates for ship with decks = decks_number
def generate_xy(decks_number):
    x = randint(0, dimensions - decks_number)
    y = randint(0, dimensions - 1)
    # Count quantity of random generation x,y
    global iterations
    iterations += 1
    return(x,y)
    
# insert horizontal ship in x,y, if there is 0
def insert_horizontal(decks_number):
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
                
# convert field with 0,1,2 to ascii (---xxx--)
def convert_to_ascii(area):
    ascii_area = [['-' for i in range(dimensions)] for i in range(dimensions)]
    for i in range(dimensions):
        for j in range(dimensions):
            if area[i][j] == 1:
                ascii_area[i][j] = 'x'
    return(ascii_area)

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

area = convert_to_ascii(area)
print_area(area)

print('\n-------------------\n')
print('Iterations: ', iterations)

