from testrecursion import Game as G

def test (did_pass):
"""Print the result of a test."""
    line_num = sys._getframe(1).f_lineno #Get the caller’s line number.
    if did_pass:
        msg = ("Test at line {0} ok.".format(line_num))
    else:
        msg = ("Test at line {0} FAILED.".format(line_num))
    print(msg)

def tests_simple():
 #Create the world
    G.create_world(8)
#basic tests
test(G.where_is_robot() == (7 , 0))
test(G.is_feasible((1, 0)))
test(G.is_feasible((6, 0)) == False)
test(G.is_feasible((0, -1))== False)
test(G.is_feasible((-1 ,0)) == False)
test(G.is_feasible((-1, -1))==False)
G.move_robot(6 , 0)
G.move_robot(5 , 0)
test(G.where_is_robot() == (5, 0))
# move the robot to the goal and t e s t whether i t i s detected
G.move_robot(4, 0)
G.move_robot(3, 0)
G.move_robot(2, 0)
G.move_robot(1, 0)
G.move_robot(0, 0)
G.move_robot(0, 1)
G.move_robot(0, 2)
G.move_robot(0, 3)
test(G.where_is_robot()==(0, 3))
test(G.goal_reached() == False)
G.move_robot(0, 4)
G.move_robot(0, 5)
G.move_robot(0, 6)
G.move_robot(0, 7)
test(G.where_is_robot()==(0, 7))
test(G.goal_reached()==True)