from Stack_linkedlist import *

class Board(list):

    def __str__(self):
        return "\n".join(" ".join(row) for row in self)

class Game(object):

    MARKER_X = "X"
    MARKER_G = "G"
    MARKER_O = "O"
    START = [0, 7]
    GOAL = [7, 0]
    default = [["O"] * 8 for _ in range (8)]
    count = 0

    def __init__(self):
        self.flag = True
        self.arena = Board(Game.default)
        self.curr_pos = Game.START[:]
        self.prev_pos = Game.START[:]
        self.arena[0][7] = Game.MARKER_G
        self.move_player()
        self.arena[1][3] = "*"
        self.arena[1][4] = "*"
        self.arena[1][5] = "*"
        self.arena[1][6] = "*"
        self.arena[1][7] = "*"
        self.arena[3][2] = "*"
        self.arena[4][2] = "*"
        self.arena[5][2] = "*"
        self.arena[6][2] = "*"
        self.arena[7][2] = "*"

    def move_player(self):
        px, py = self.prev_pos
        cx, cy = self.curr_pos
        if (-1 < cx < 8) and (-1 < cy < 8):
            self.arena[py][px] = Game.MARKER_O
            self.arena[cy][cx] = Game.MARKER_X
            # self.arena[0][4] = Game.MARKER_G
            # print(self.curr_pos)
            print(str(self.arena))
            print(" ")
        else:
            self.curr_pos = self.prev_pos[:]
            #self.curr_pos.pop()
            self.move_player()

    def play(self):
        print("You are: \nX")
        while self.flag:
            Game.count+=1
            if self.curr_pos!=Game.GOAL:
                print(self.curr_pos)
                print (Game.GOAL)
                #dont need this if in linked list
            # if self.curr_pos[1]== 4:
                self.prev_pos = self.curr_pos[:]
                self.curr_pos[1]= self.curr_pos[1]-1
                self.move_player()
            if self.curr_pos[1]==0:
                self.prev_pos = self.curr_pos[:]
                self.curr_pos[0] = self.curr_pos[0] + 1
                self.move_player()
            # if self.curr_pos[0]==4:
            if self.curr_pos==Game.GOAL:
                print("You've reached the goal!")
                Game.count+=1
                print(Game.count)
                self.flag=False

    def printArena(self):
        print(str(self.arena))
        print(self.curr_pos[1])

my_game = Game()
my_game.play()

