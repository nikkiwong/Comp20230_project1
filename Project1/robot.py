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

w = 70

def setup():
    size(800, 600)

def draw():
    x, y = 0,0
    for row in grid:
        for col in row:
            rect(x, y, w, w)
            x = x + w
        y = y + w
        x = 0