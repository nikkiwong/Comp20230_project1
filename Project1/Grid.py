import numpy as np
from Stack_linkedlist import Stack
import sys

class Game(object):
    # This is an automated robot where he roams the world
    # automatically without the need for any input
    MARKER_X = "X"
    MARKER_G = "G"
    MARKER_V = "V"
    MARKER_1 = "1"
    count = 0
    sa = Stack()
    GOAL = [7, 0]
    START = [0, 7]

    def create_word(self, s):
        size = s
        default = [["O"] * size for n in range(size)]
        default[1][3] = "*"
        default[1][4] = "*"
        default[1][5] = "*"
        default[1][6] = "*"
        default[1][7] = "*"

        #this wall blocks the goal from being reached
        # default[0][6] = "*"

        default[3][2] = "*"
        default[4][2] = "*"
        default[5][2] = "*"
        default[6][2] = "*"
        default[7][2] = "*"
        return np.array(default)

    def __init__(self, s):
        self.flag = True
        self.goal = Game.GOAL
        self.r2d2 = Game.START
        self.size = s
        self.arena = self.create_word(self.size)
        print(str(self.arena))
        self.find_path()




    def where_is_robot(self):
        return self.r2d2

    def is_feasible(self, x, y):
        # pass
        # print(" ")
        # print self.arena[x][y]
        # print("is feasible ", y, x)

        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            # print("We have exceeded boundary")
            # print("Return false")
            return False

        elif self.arena[x][y] == "*" or self.arena[x][y] == "V" or self.arena[x][y] == "1":
            # print("We have hit a wall")
            # print("return false")
            return False

        else:
            # print("return True")
            return True

    # def co_ords(self, x, y):

    def move_robot(self, cx, cy):
        # #get oo-ordinates for the goal, previous position and the robots position
        # print(Game.sa)
        gx, gy = self.goal
        # cx, cy = self.r2d2
        # Game.sa.push([cx, cy])
        # px, py = Game.sa.peek()
        # print(Game.sa)
        # print(" ")
        # print("previous: ", px, py)
        #
        # print("robot: ", (cx, cy))
        # print("robot: ", self.r2d2)
        # print("top: ", Game.sa.top())

        if (-1 < cx < self.size) and (-1 < cy < self.size) and self.arena[cy][cx] == "O" or self.arena[cy][cx] == "G":
            Game.sa.push([cx, cy])
            # print("inside loop:", cx, cy)
            px, py = Game.sa.peek()
            # print("previous: ", px, py)
            self.arena[py][px] = Game.MARKER_1
            self.arena[gy][gx] = Game.MARKER_G
            self.arena[cy][cx] = Game.MARKER_X
            # print(str(self.arena))
            # print(" ")

        else:
            # print(Game.sa)
            # print(str(self.arena))
            # print(" ")
            bx, by = Game.sa.top()
            # print("Game top: ", bx, by)
            if (-1 < cx < self.size) and (-1 < cy < self.size) and self.arena[cy][cx]!="*":
                self.arena[by][bx] = Game.MARKER_V
            Game.sa.pop()
            cx, cy = Game.sa.top()

            self.arena[cy][cx] = Game.MARKER_X
            # print("after pop top: ", cx, cy)
            # print("robot", cx, cy)
            self.r2d2[0] = cx
            self.r2d2[1] = cy
            # print("r2d2 after pop", self.r2d2)
            px, py = Game.sa.peek()
            # self.move_robot()
            # print(str(self.arena))


    def find_path(self):
        #if the stack is empty, then set the start location for the robot on the map
        if Game.sa.top() == []:
            self.move_robot(self.r2d2[0], self.r2d2[1])
        #if the robot location and the goal location is the same then print out you have found the goal!!
        if self.r2d2 == self.goal:
            print(" ")
            print("You have found the goal!")
            print (" ")
            print(str(self.arena))
            return True
        #otherwise, check if the current location of the robot is valid, this is
        # elif self.r2d2 == "X":
        #     print("no path")
        #     if self.is_feasible(self.r2d2[1] - 1, self.r2d2[0])==False:
        #         print("No path to goal.")
        #     return False

        else:
            # print("robot: ", self.r2d2)
            # print("game top: ", Game.sa.top())
            # print("game size: ", Game.sa.size())
            if self.is_feasible(self.r2d2[1]-1,self.r2d2[0])==True:
                # self.move_robot()
                self.r2d2[1]-=1
                self.move_robot(self.r2d2[0], self.r2d2[1])
                return self.find_path()
            if self.is_feasible(self.r2d2[1], self.r2d2[0]+1) == True:
                self.r2d2[0]+=1
                self.move_robot(self.r2d2[0], self.r2d2[1])
                return self.find_path()
            if self.is_feasible(self.r2d2[1]+1, self.r2d2[0]) == True:
                self.r2d2[1]+=1
                self.move_robot(self.r2d2[0], self.r2d2[1])
                return self.find_path()
            if self.is_feasible(self.r2d2[1], self.r2d2[0]-1) == True:
                self.r2d2[0]-=1
                self.move_robot(self.r2d2[0], self.r2d2[1])
                return self.find_path()
            if Game.sa.size() == 1:
                print(" ")
                print("The are no possible paths to reach the goal. :( ")
                print(" ")
                print(str(self.arena))
                return False
            else:
                self.move_robot(self.r2d2[0], self.r2d2[1])
                return self.find_path()


    def goal_reached(self):
        # print(self.r2d2, self.goal)
        return self.r2d2==self.goal

    def __repr__(self):
        return self.arena.__repr__()

A = Game(8)
A
