# https://www.geeksforgeeks.org/check-if-a-given-sequence-of-moves-for-a-robot-is-circular-or-not/

# Complete the function below.
N = 0
E = 1
S = 2
W = 3
def isCircular(path):
 
    # Initialize starting point for robot as (0, 0) and starting
    # direction as N North
    x = 0
    y = 0
    dir = N
 
    # Traverse the path given for robot
    for i in range(len(path)):
 
        # Find current move
        move = path[i]
 
        # If move is left or right, then change direction
        if move == 'R':
            dir = (dir + 1)%4
        elif move == 'L':
            dir = (dir - 1)%4
 
        # If move is Go, then change x or y according to
        # current direction
        else:    # if move == 'G'
            if dir == N:
                y += 1
            elif dir == E:
                x += 1
            elif dir == S:
                y -= 1
            else:
                x -= 1
 
    return (x == 0 and y == 0)

def doesCircleExist(commands):
    res = []
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    for command in commands:
        if "G" not in command:
            res += "YES",
            continue
        new = command * 4
        di, p = 0, (0,0)
        for c in new:
            if c == "G":
                p = (p[0]+dirs[di][0], p[1]+dirs[di][1])
            elif c == "R":
                di = (di + 1) % 4
            elif c == "L":
                di = (di - 1) % 4
        if p == (0,0):
            res += "YES",
        else:
            res += "NO",
    return res
# def doesCircleExist(commands):
#     res = []
#     for command in commands:
#         if isCircular(command*4):
#             res += "YES",
#         else:
#             res += "NO",
#     return res

if __name__ == '__main__':
    from minitest import *

    with test(doesCircleExist):
        doesCircleExist(["RGGRGGRGGRG"]).must_equal(["NO"])
        doesCircleExist(["LR"]).must_equal(["YES"])



