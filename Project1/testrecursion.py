import numpy as np
from Stack_linkedlist import Stack


class Game(object):

    MARKER_X = "X"
    MARKER_G = "G"
    MARKER_V = "V"
    MARKER_1 = "1"
    size = 8
    default = [["O"] * size for n in range(size)]
    default[1][3] = "*"
    default[1][4] = "*"
    default[1][5] = "*"
    default[1][6] = "*"
    default[1][7] = "*"
    default[3][2] = "*"
    default[4][2] = "*"
    default[5][2] = "*"
    default[6][2] = "*"
    default[7][2] = "*"
    GOAL = [7, 0]
    START = [0, 7]
    PREV = [0, 7]
    count = 0
    sa = Stack()


    def __init__(self):
        self.flag = True
        self.prev = Game.PREV
        self.goal = Game.GOAL
        self.r2d2 = Game.START
        self.arena = np.array(Game.default)
        self.find_path()



    def where_is_robot(self):
        pass
        return self.r2d2

    def is_feasible(self, x, y):
        # print self.arena[x][y]
        if self.arena[x][y] == "*" or self.arena[x][y] == "V" or self.arena[x][y] == 1:
            print("We have hit a wall")
            print("return false")
        if (-1 < self.arena[x] < Game.size) and (-1 < self.arena[y] < Game.size):
            print("We have exceeded boundary")
            print("Return false")
        if (-1 < self.arena[x] < Game.size) and (-1 < self.arena[y] < Game.size):
            print("We have exceeded boundary")
            print("Return false")

    def move_robot(self):
        # #get oo-ordinates for the goal, previous position and the robots position
        gx, gy = self.goal
        cx, cy = self.r2d2
        Game.sa.push([cx, cy])
        px, py = Game.sa.peek()

        print("previous: ", px, py)

        print("robot: ", self.r2d2)

        if (-1 < cx < Game.size) and (-1 < cy < Game.size):
            if self.arena[cy][cx] == "O":
                self.arena[py][px] = Game.MARKER_1
                print(self.arena[py][px])
                self.arena[gy][gx] = Game.MARKER_G
                self.arena[cy][cx] = Game.MARKER_X
                print(str(self.arena))
                print(" ")
                Game.sa
                Game.sa.peek()

        else:
            top = Game.sa.top()
            bx, by = top
            print("Game top: ", top)
            self.arena[by][bx] = Game.MARKER_V
            Game.sa.pop()
            cx, cy = Game.sa.top()
            print("robot", cx, cy)
            # self.move_robot()

    def find_path(self):

        self.move_robot()

        self.is_feasible(self.r2d2[1], self.r2d2[0])
        self.r2d2[1] = self.r2d2[1]-1
        # print(self.r2d2)

        self.move_robot()

        self.is_feasible(self.r2d2[1], self.r2d2[0])
        self.r2d2[1] = self.r2d2[1]-1

        self.move_robot()

        self.is_feasible(self.r2d2[1], self.r2d2[0])
        self.r2d2[1] = self.r2d2[1]-1

        self.move_robot()
        # if self.r2d2 == self.goal:
        #     print("You have found the goal")
        #     return True
        # if r2d2[0]:

    def __repr__(self):
        return self.arena.__repr__()


A = Game()

A
# # print(A[1])
# # print(B[0])
# i=0
# j=0
#
# for row in A.arena: #for each subset array in the array
#     #use this to select the row
#     # print("row: ", row[0]) #prints each row starting from top
#     for elem in row: #for each element in the array
#         # while i<len(grid[i]) and j<len(grid[i]):
#         if elem == "O": #prints out value of col, not the co-ordinates
#             print("we have empty space")