from Stack import *
from linked_list import *


# making a grid
# from cmath import rect
class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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


# def link_grid():
#     '''Putting each value of the array of arrays into a linked list'''
#     x, y = 0, 0
#     L = LinkedList()
#     L.add_head(Node(grid[x][y]))
#     for row in grid:
#         for col in row:
#             L.add_tail(Node(grid[row][col]))
#         print(L)


# You have arrays for original values of the grid,
# linked list for temporary values of the array that can be replaced with the value of the robot.
#linked list can contain the index value of the array and the co-ordination pairs
# if you assign new value to a grid, and you want to go back, how do you get the value of that grid when you go back recursively?


grid = [[0] * 8 for n in range(8)]
# goal c-ords
grid[0][7] = "*"

# start co-ords
grid[7][0] = 2

# wall
grid[1][3] = 1
grid[1][4] = 1
grid[1][5] = 1
grid[1][6] = 1
grid[1][7] = 1
grid[3][2] = 1
grid[4][2] = 1
grid[5][2] = 1
grid[6][2] = 1
grid[7][2] = 1

# def setup():
#     size(800,600)
# Robot.goal()
# Robot.start()
# link_grid()
#

# def robot():
#     x, y = 0, 0
#     while x < 8 and y < 8:
#         for row in grid:
#             # for col in row:
#                 value = 1
#                 print[[n[x] for n[y] in grid]]
                # Stack.push(int(grid[row][col]))
                # Stack.pop()
                # elif grid[row][col] == 9:
                #     print("You have reached the goal!")
                # else:
                #     grid[row][col] = 2
                #     print("hello")
                #     grid[row - 1][col - 1] = 0


x, y = 7, 0
for row in grid:
    for col in row:
        if col == 1:
            continue
        elif col == 9:
            print("GOAL!")
        else:
           if col == 0:
                col = 2
                #col-1=0
        print(row)
