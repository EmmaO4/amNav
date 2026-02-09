class Robot:

    # init robot with given map and modifiable start location 
    def __init__(self, map_obj = None, start = None):
        self.map_obj = map_obj
        if start:
            self.start = start
        else:
            start = (0, 0)
        self.position = self.start

    ''' --- State Access ---
    return current robot pos (row, col) 
    '''
    def get_position(self):
        return self.position

    # return if robot at goal
    def at_goal(self):
        pass

    ''' --- Movement ---
    robot navigational movement options: ('up' : 'w', 'down' : 's', 'left' : 'a', 'right' : 'd')
    '''
    def move(self, direction):
        pass

    ''' --- Navigation Helpers ---
    # return list of valid directions 
    '''
    def get_possible_moves(self):
        pass

    def reset_position(self, position = None):
        pass

    ''' --- Sensors / Awareness ---
    utility for blind movement without map 
    '''
    def scan_surroundings(self):
        pass

    # extra functionality
    def detect_obstacle(self, direction):
        pass

    def __str__(self):
        return f"Robot at {self.position}, goal at {self.map_obj.goal}"