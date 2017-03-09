from Stack_linkedlist import *
from linked_list import *
import numpy as np


# # making a grid
# # from cmath import rect
# def Goal(x, y):
#     A = createWorld()


def createWorld(size):
    s = size
    grid = [[0] * s for n in range(s)]
    # goal c-ords
    grid[0][7] = "G"
    # start co-ords
    grid[7][0] = "R"

    # wall
    grid[1][3] = "*"
    grid[1][4] = "*"
    grid[1][5] = "*"
    grid[1][6] = "*"
    grid[1][7] = "*"
    grid[3][2] = "*"
    grid[4][2] = "*"
    grid[5][2] = "*"
    grid[6][2] = "*"
    grid[7][2] = "*"

    A = np.array(grid)
    return A, size, grid

def where_is_robot():
    pass

def is_feasible(x, y):
    pass

def move_robot(x, y):
    pass
def goal_reached():
    pass


A = createWorld(8)
print(A[0])
print(A[1])


grid = A[0]
i=0
j=0
for row in grid: #for each subset array in the array
    #use this to select the row
    # print("row: ", row[0]) #prints each row starting from top
    for elem in row: #for each element in the array
        # while i<len(grid[i]) and j<len(grid[i]):
        if elem == "*": #prints out value of col, not the co-ordinates
            print("we hit a wall")
        # if elem == '0':
        #     if (grid[i][j+1] == 0):
        #         continue
        #     if (grid)

#once it selects it needs to push into stack
#
# def f(grid):
#
#     """function returns the series of its argument
#
#     Assumes that its argument is an integer
#     Uses a recursive definition"""
#
#     if grid == 0:
#         return 2
#     else:
#         x = x + f(x - 1)
#         print(x)
#         return x


            # You have arrays for original values of the grid,
# linked list for temporary values of the array that can be replaced with the value of the robot.
#linked list can contain the index value of the array and the co-ordination pairs
# if you assign new value to a grid, and you want to go back, how do you get the value of that grid when you go back recursively?


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


# x, y = 7, 0
# for row in grid:
#     for col in row:
#         if col == 1:
#             continue
#         elif col == 9:
#             print("GOAL!")
#         else:
#            if col == 0:
#                 col = 2
#                 #col-1=0


