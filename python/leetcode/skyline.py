# https://leetcode.com/problems/the-skyline-problem/
# http://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/

def cal_skyline_points(buildings):
    result = []
    for building in buildings:
        result = merge_two_skylines(result, get_skyline_from_building(building))

    return result

def merge_two_skylines(first_skyline, second_skyline):
    first_height, second_height = 0, 0
    result = []
    while len(first_skyline) > 0 or len(second_skyline) > 0:
        if len(first_skyline) == 0:
            result += second_skyline
            break
        if len(second_skyline) == 0:
            result += first_skyline
            break
        current_point = None
        if first_skyline[0][0] < second_skyline[0][0]:
            current_point = first_skyline.pop(0)
            first_height = current_point[1]
        else:
            current_point = second_skyline.pop(0)
            second_height = current_point[1]
        will_add = (current_point[0], max(first_height, second_height))
        if len(result) == 0 or result[-1][1] != will_add[1]:
            result.append(will_add)
    return result


def get_skyline_from_building(building):
    return [(building[0], building[2]), (building[1],0)]



if __name__ == '__main__':
    from minitest import *

    with test(cal_skyline_points):
        buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        cal_skyline_points(buildings).must_equal(
                [(2,10),(3,15),(7,12),(12,0),(15,10),(20,8),(24,0)])
        pass

    with test(get_skyline_from_building):
        get_skyline_from_building([2,9,10]).must_equal( [(2, 10), (9, 0)] )

    # with test(merge_two_skylines):
    #     cal_left_join_point([2,9,10],[3,7,15]).must_equal(())