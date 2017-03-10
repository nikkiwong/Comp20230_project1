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

    # default[1][0] = "*"
    # default[1][1] = "*"

    default[0][1] = "*"
    default[1][1] = "*"

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
        print(" ")
        print self.arena[x][y]
        print("is feasible ", y, x)
        if self.arena[x][y] == "*" or self.arena[x][y] == "V" or self.arena[x][y] == "1":
            print("We have hit a wall")
            print("return false")
            return False

        elif x < 0 or x >= Game.size or y < 0 or y >= Game.size:
            print("We have exceeded boundary")
            print("Return false")
            return False

        else:
            print("return True")
            return True

    def move_robot(self):
        # #get oo-ordinates for the goal, previous position and the robots position
        # print(Game.sa)
        gx, gy = self.goal
        cx, cy = self.r2d2
        # Game.sa.push([cx, cy])
        # px, py = Game.sa.peek()
        print(Game.sa)
        print(" ")
        # print("previous: ", px, py)

        print("robot: ", (cx, cy))
        print("robot: ", self.r2d2)
        print("top: ", Game.sa.top())

        if (-1 < cx < Game.size) and (-1 < cy < Game.size) and self.arena[cy][cx] == "O" or self.arena[cy][cx] == "G":
            Game.sa.push([cx, cy])
            print("inside loop:", cx, cy)
            px, py = Game.sa.peek()
            self.arena[py][px] = Game.MARKER_1
            self.arena[gy][gx] = Game.MARKER_G
            self.arena[cy][cx] = Game.MARKER_X
            print(str(self.arena))
            print(" ")

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

            self.arena[cy][cx] = Game.MARKER_X
            print("after pop top: ", cx, cy)
            print("robot", cx, cy)
            self.r2d2[0] = cx
            self.r2d2[1] = cy
            print("r2d2 after pop", self.r2d2)
            px, py = Game.sa.peek()
            # self.move_robot()
            print(str(self.arena))


    def find_path(self):
        print("number 1 r2d2:", self.r2d2, "; goal: ", self.goal)
        self.move_robot()
        print("after first move r2d2:", self.r2d2, "; goal: ", self.goal)
        if self.r2d2 == self.goal:
            print("You have found the goal")
            return True
        elif self.is_feasible(self.r2d2[1], self.r2d2[0])==False:
            if self.is_feasible(self.r2d2[1] - 1, self.r2d2[0])==False:
                print("No path to goal.")
            return False
        else:
            if self.is_feasible(self.r2d2[1]-1,self.r2d2[0])==True:
                # self.move_robot()
                self.r2d2[1]-=1
                # self.move_robot()
                return self.find_path()
            if self.is_feasible(self.r2d2[1], self.r2d2[0]+1) == True:
                self.r2d2[0]+=1
                # self.move_robot()
                return self.find_path()
            if self.is_feasible(self.r2d2[1]+1, self.r2d2[0]) == True:
                self.r2d2[1]+=1
                # self.move_robot()
                return self.find_path()
            if self.is_feasible(self.r2d2[1], self.r2d2[0]-1) == True:
                self.r2d2[0]-=1
                # self.move_robot()
                return self.find_path()
            else:
                # self.move_robot()
                return self.find_path()

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