from Grid import Game
import sys

def test(did_pass):
#Print the result of a test
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(line_num))
    else:
        msg = ("Test at line {0} FAILED.".format(line_num))
    print(msg)

def tests_simple():
 #Create the world
    #when you print the game with a number it creates
    #the world and runs it automatically
    G = Game(9)
#basic tests
    #because of the automatic running of the game once
    #you call it, the robot has already made its way to the goal
    #therefore the robot should be at the goal if its working and if the goal is not blocked
    #with the default walls set up

    #in this test the robot starts from the goal and works backwards to the start.
    test(G.where_is_robot()==[7, 0])
    test(G.goal_reached() == True)
    test(G.is_feasible(1, 0)==False)
    test(G.is_feasible(6, 0) == False)
    test(G.is_feasible(0, -1)== False)
    test(G.is_feasible(-1 ,0) == False)
    test(G.is_feasible(-1, -1)==False)
    G.move_robot(6, 0)
    G.move_robot(5, 0)
    test(G.where_is_robot() == [5, 0])
    #move robot towards the start and see if the goal and start are detected
    G.move_robot(4, 0)
    G.move_robot(3, 0)
    G.move_robot(2, 0)
    G.move_robot(1, 0)
    G.move_robot(0, 0)
    G.move_robot(0, 1)
    G.move_robot(0, 2)
    G.move_robot(0, 3)
    test(G.where_is_robot()==[0, 3])
    test(G.goal_reached() == False)
    G.move_robot(0, 4)
    G.move_robot(0, 5)
    G.move_robot(0, 6)
    G.move_robot(0, 7)
    test(G.where_is_robot()==[0, 7])
    test(G.goal_reached()!=True)
    test(G.r2d2 == G.START)

tests_simple()