class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def start_pos(self):
        self.grid[7][0] = "r"
        # def goal(self):
        #     grid[0][7] = "goal"

        # def start(self):
        #     grid[7][0] = "start"
