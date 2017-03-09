import numpy as np
from Stack_linkedlist import Stack


class Game(object):

    MARKER_X = "X"
    MARKER_G = "G"
    MARKER_V = "V"
    MARKER_1 = "1"
    size = 8
    default = [["O"] * size for n in range(size)]
    default[0][0] = "*"
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
    count = 0
    sa = Stack()


    def __init__(self):
        self.flag = True
        self.goal = Game.GOAL
        self.r2d2 = Game.START
        self.arena = np.array(Game.default)
        self.find_path()



    def where_is_robot(self):
        pass
        return self.r2d2

    def is_feasible(self, x, y):
        # pass
        print self.arena[x][y]
        print ("is feasible ", y, x)
        if self.arena[y][x] == "*" or self.arena[y][x] == "V" or self.arena[y][x] == 1:
            print("We have hit a wall")
            print("return false")
        elif (-1 < self.arena[x] < Game.size) and (-1 < self.arena[y] < Game.size):
            print("We have exceeded boundary")
            print("Return false")
        elif (-1 < self.arena[x] < Game.size) and (-1 < self.arena[y] < Game.size):
            print("We have exceeded boundary")
            print("Return false")
        else:
            print ("return True")
            return True

    def move_robot(self):
        # #get oo-ordinates for the goal, previous position and the robots position
        print(Game.sa)
        gx, gy = self.goal
        cx, cy = self.r2d2
        Game.sa.push([cx, cy])
        px, py = Game.sa.peek()
        print(" ")
        print("previous: ", px, py)

        print("robot: ", self.r2d2)
        print("top: ", Game.sa.top())

        if (-1 < cx < Game.size) and (-1 < cy < Game.size) and self.arena[cy][cx] == "O" or self.arena[cy][cx] == "1":
                self.arena[py][px] = Game.MARKER_1
                self.arena[gy][gx] = Game.MARKER_G
                self.arena[cy][cx] = Game.MARKER_X
                print(str(self.arena))
                print(" ")
                # Game.sa.peek()

        else:
            print(Game.sa)
            print(str(self.arena))
            print(" ")
            bx, by = Game.sa.top()
            print("Game top: ", bx, by)
            if (-1 < cx < Game.size) and (-1 < cy < Game.size) and self.arena[cy][cx]!="*":
                self.arena[by][bx] = Game.MARKER_V
            Game.sa.pop()
            cx, cy = Game.sa.top()
            # if self.arena[cy][cx]=="*":
            #     print ("after pop wall", cx, cy)
            #     Game.sa.pop()
            #     cx, cy = Game.sa.top()
            self.arena[cy][cx] = Game.MARKER_X
            print("after pop top: ", cx, cy)
            print("robot", cx, cy)
            self.r2d2 = cx, cy
            px, py = Game.sa.peek()
            # self.move_robot()
            print(str(self.arena))


    def find_path(self):
        if self.r2d2 == self.goal:
            print("You have found the goal")
            return True
        if r2d2[0]:


        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[1] = self.r2d2[1]-1
        # # print(self.r2d2)
        # print("going to move robot")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[1] = self.r2d2[1]-1
        # print("going to move robot")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[1] = self.r2d2[1]-1
        # print("going to move robot")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[1] = self.r2d2[1] - 1
        # print("going to move robot")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[1] = self.r2d2[1] - 1
        # print("going to move robot")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[1] = self.r2d2[1] - 1
        # print("going to move robot")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[1] = self.r2d2[1] + 1
        # print("r2d2: ", self.r2d2)
        # print("going to move robot")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # # print("across")
        # # print(self.r2d2[0])
        # self.r2d2[0] = self.r2d2[0] + 1
        # print("r2d2: ", self.r2d2)
        # print("across")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[0] = self.r2d2[0] + 1
        #
        # self.move_robot()
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[0] = self.r2d2[0] + 1
        # print("r2d2: ", self.r2d2)
        # print("across")
        # self.move_robot()
        #
        # self.is_feasible(self.r2d2[1], self.r2d2[0])
        # self.r2d2[0] = self.r2d2[0] + 1
        #
        # self.move_robot()


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