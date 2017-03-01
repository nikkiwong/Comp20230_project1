from Stack import *

class Board(list):

    def __str__(self):
        return "\n".join(" ".join(row) for row in self)


class Game(object):

    MARKER_X = "X"
    MARKER_G = "G"
    MARKER_O = "O"
    START = [0, 4]
    GOAL = [4, 0]
    DEFAULT = [["O"] * 5 for _ in range(5)]

    def __init__(self):
        self.flag = True
        self.arena = Board(Game.DEFAULT)
        self.curr_pos = Game.START[:]
        self.prev_pos = Game.START[:]
        self.arena[0][4] = Game.MARKER_G
        self.move_player()

    def move_player(self):
        px, py = self.prev_pos
        cx, cy = self.curr_pos
        if (-1 < cx < 5) and (-1 < cy < 5):
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
            if self.curr_pos!=Game.GOAL:
                print(self.curr_pos)
                print (Game.GOAL)
                self.prev_pos = self.curr_pos[:]
                self.curr_pos[1]= self.curr_pos[1]-1
                self.move_player()
            if self.curr_pos[1]==0:
                print("we've reached the top")
                print(self.curr_pos)
                self.prev_pos = self.curr_pos[:]
                self.curr_pos[0] = self.curr_pos[0] + 1
                self.move_player()
            if self.curr_pos[0]==4:
                if self.curr_pos==Game.GOAL:


                # elif self.curr_pos[1]==4:
                #     pass
            # else:
                    print("You've reached the goal!")
                    self.flag=False

    def printArena(self):
        print(str(self.arena))
        print(self.curr_pos[1])

my_game = Game()
my_game.play()