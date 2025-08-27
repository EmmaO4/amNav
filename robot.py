class Robot:

    # init robot with given map and modifiable start location 
    def __init__(self, map_obj, start=None):
        pass

    ''' --- State Access --- '''
    # return current robot pos (row, col) 
    def get_position(self):
        pass

    # return if robot at goal
    def at_goal(self):
        pass

    ''' --- Movement --- '''
    # robot navigational movement options: ('up' : 'w', 'down' : 's', 'left' : 'a', 'right' : 'd')
    def move(self, direction):
        pass

    ''' --- Navigation Helpers --- '''
    # return list of valid directions 
    def get_possible_moves(self):
        pass

    def reset_position(self, position=None):
        pass

    ''' --- Sensors / Awareness --- '''
    # utility for blind movement without map 
    def scan_surroundings(self):
        pass

    # extra functionality
    def detect_obstacle(self, direction):
        pass
