"""
This file to test maze solver patterns and algorithms as well as practice for those algos
"""
mouse = 2
maze =  [
        [1,1,0,1],
        [1,0,0,1],
        [0,0,1,1],
        [0,1,1,1],
        [0,0,0,9]
        ]

# calculates the start of mouse by scanning from top - down. Expects entrance to be in first list.
def calculate_start():
    for outer in range(len(maze)):
        for inner in range(len(maze)):
            if maze[outer][inner] == 0:
                return outer, inner

start_position = calculate_start()
print(f'mouse start position: {start_position}')

x_axis  = start_position[0]
y_axis  = start_position[1]

LEFT    = x_axis - 1
RIGHT   = 1 + x_axis
UP      = y_axis - 1
DOWN    = 1 + y_axis

move = 0

def collision_check():
    valid_movement = True
    # booleans might be unecessary
    # conditions are backwards
    if LEFT < 0:
        move = 1
        # return not valid_movement
    elif RIGHT < 0:
        move = 2
        # return not valid_movement
    elif UP < 0:
        move = 3
        # return not valid_movement
    elif DOWN < 0:
        move = 4
        # return not valid_movement
    else:
        move = 5
        # return valid_movement

# increment position of x, y by 1 appropriately for each axis.
def automate_movement():
    curr_position = start_position
    
    # indecies are wrong here
    while maze[x_axis][y_axis] != 9:
        if move == 1:
            curr_position = maze[x_axis][LEFT]
        if move == 2:
            curr_position = maze[x_axis][RIGHT]
        if move == 3:
            curr_position = maze[UP][y_axis]
        if move == 4:
            curr_position = maze[DOWN][y_axis]





'''
psuedocode: 
        while curr pos is not GOAL = 9:
        check validity of movement(up, left, down, right)
        if valid movement:
            go that movement (ex: perform DOWN)

'''



"""
big maze: 
[ 
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
"""