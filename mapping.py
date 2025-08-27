class Map:

    # attrs to set up an instance: grid = map, start and goal locations -- start/goal to be modified
    def __init__(self, grid, start = (0, 0), goal = (0, 0)):
        pass

    # get current position stored at row, col
    def get_value(self, position):
        pass

    # check if given pos is goal
    def is_goal(self, position):
        pass

    # check if position inputted is within bounds of map
    def in_bounds(self, position):
        pass

    # check if position of interest is free for movement -- maybe replace with simple err saying can't move there in movement method
    def is_free(self, position):
        pass

    # update starting pos
    def set_start(self, position):
        pass

    # update goal pos
    def set_goal(self, position):
        pass

    # return a list of valid neighboring movements -- extra functionality
    def is_neighbors(self, position):
        pass

    # display current map -- extra funcitonality
    def display(self):
        pass