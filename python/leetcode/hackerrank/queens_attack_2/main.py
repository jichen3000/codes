def is_at_top_left(origin, relative):
    return relative[0] - origin[0] == -(relative[1] - origin[1]) and relative[0] > origin[0]
def is_at_top_right(origin, relative):
    return relative[0] - origin[0] == relative[1] - origin[1] and relative[0] > origin[0]
def is_at_bottom_right(origin, relative):
    return relative[0] - origin[0] == -(relative[1] - origin[1]) and relative[0] < origin[0]
def is_at_bottom_left(origin, relative):
    return relative[0] - origin[0] == relative[1] - origin[1] and relative[0] < origin[0]

def is_at_top_middle(origin, relative):
    return relative[0] >  origin[0] and relative[1] == origin[1]
def is_at_middle_right(origin, relative):
    return relative[0] ==  origin[0] and relative[1] > origin[1]
def is_at_bottom_middle(origin, relative):
    return relative[0] <  origin[0] and relative[1] == origin[1]
def is_at_middle_left(origin, relative):
    return relative[0] ==  origin[0] and relative[1] < origin[1]


def get_closer_point(origin, p1, p2):
    if p1 == None: return p2
    if p2 == None: return p1
    if p1 == None and p2 == None:
        raise Exception("p1 and p2 are all None!")
    if abs(p1[0]-origin[0]) + abs(p1[0]-origin[0]) > abs(p2[0]-origin[0]) + abs(p2[0]-origin[0]):
        return p2
    else:
        return p1

def get_all_possible_points_count(origin, neighbores, n):
    count_list = []
    closest_top_left = neighbores[(1,-1)]
    if closest_top_left:
        count_list.append(closest_top_left[0] - origin[0] - 1)
    else:
        count_list.append(min(n-origin[0], origin[1]-1))

    closest_top_right = neighbores[(1,1)]
    if closest_top_right:
        count_list.append(closest_top_right[0] - origin[0] - 1)
    else:
        count_list.append(min(n-origin[0], n-origin[1]))

    closest_bottom_right = neighbores[(-1,1)]
    if closest_bottom_right:
        count_list.append(origin[0] - closest_bottom_right[0] - 1)
    else:
        count_list.append(min(origin[0]-1, n-origin[1]))

    closest_bottom_left = neighbores[(-1,-1)]
    if closest_bottom_left:
        count_list.append(origin[0] - closest_bottom_left[0] - 1)
    else:
        count_list.append(min(origin[0]-1, origin[1]-1))

    closest_top_middle = neighbores[(1,0)]
    if closest_top_middle:
        count_list.append(closest_top_middle[0] - origin[0] - 1)
    else:
        count_list.append(n - origin[0])

    closest_middle_right = neighbores[(0,1)]
    if closest_middle_right:
        count_list.append(closest_middle_right[1] - origin[1] - 1)
    else:
        count_list.append(n - origin[1])

    closest_bottom_middle = neighbores[(-1,0)]
    if closest_bottom_middle:
        count_list.append(origin[0] - closest_bottom_middle[0] - 1)
    else:
        count_list.append(origin[0] - 1)

    closest_middle_left = neighbores[(0,-1)]
    if closest_middle_left:
        count_list.append(origin[1] - closest_middle_left[1] -  1)
    else:
        count_list.append(origin[1] - 1)

    # print("count_list:{}".format(count_list))
    return sum(count_list)

n,k = map(int, raw_input().strip().split(' '))
queen_point = map(int, raw_input().strip().split(' '))
#queen_point[1] = n+1 - queen_point[1]
neighbores = {(i,j):None for i in range(-1, 2) for j in range(-1, 2)}
for a0 in xrange(k):
    obstacle_point = map(int, raw_input().strip().split(' '))
    #obstacle_point[1] = n+1 - obstacle_point[1]
    if is_at_top_left(queen_point, obstacle_point):
        neighbores[(1,-1)] = get_closer_point(queen_point, neighbores[(1,-1)], obstacle_point)
    elif is_at_top_right(queen_point, obstacle_point):
        neighbores[(1,1)] = get_closer_point(queen_point, neighbores[(1,1)], obstacle_point)
    elif is_at_bottom_right(queen_point, obstacle_point):
        neighbores[(-1,1)] = get_closer_point(queen_point, neighbores[(-1,1)], obstacle_point)
    elif is_at_bottom_left(queen_point, obstacle_point):
        neighbores[(-1,-1)] = get_closer_point(queen_point, neighbores[(-1,-1)], obstacle_point)
    elif is_at_top_middle(queen_point, obstacle_point):
        neighbores[(1,0)] = get_closer_point(queen_point, neighbores[(1,0)], obstacle_point)
    elif is_at_middle_right(queen_point, obstacle_point):
        neighbores[(0,1)] = get_closer_point(queen_point, neighbores[(0,1)], obstacle_point)
    elif is_at_bottom_middle(queen_point, obstacle_point):
        neighbores[(-1,0)] = get_closer_point(queen_point, neighbores[(-1,0)], obstacle_point)
    elif is_at_middle_left(queen_point, obstacle_point):
        neighbores[(0,-1)] = get_closer_point(queen_point, neighbores[(0,-1)], obstacle_point)

# print("neighbores:{}".format(neighbores))
# cat test1.txt | python main.py # 10
print(get_all_possible_points_count(queen_point, neighbores, n))

# if __name__ == '__main__':
#     from minitest import *

#     with test(get_closer_point):
#         get_closer_point((0,0),(1,1),(2,2)).p()