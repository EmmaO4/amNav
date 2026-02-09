class Map:

    # attrs to set up an instance: grid = map, start and goal locations -- start/goal to be modified
    def __init__(self, grid, goal = (0, 0)):
        self.grid = grid 
        self.goal = goal

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

    # display current map -- extra funcitonality ?
    def display(self, robot_pos=None):
        """Print the map with robot and goal positions."""
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        for r in range(rows):
            row_str = ""
            for c in range(cols):
                if robot_pos is not None and (r,c) == robot_pos:
                    row_str += "R "
                elif (r,c) == self.goal:
                    row_str += "G "
                elif self.grid[r][c] == 1:
                    row_str += "1 "
                else:
                    row_str += "0 "
            print(row_str)  # Python 2 print statement