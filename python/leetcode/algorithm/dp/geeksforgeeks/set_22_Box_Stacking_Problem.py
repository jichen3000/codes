from itertools import permutations
def solve(boxes):
    all_boxes = [cur for box in boxes for cur in permutations(box)]
    n = len(all_boxes)
    if n == 0: return 0
    all_boxes.sort()
    dp = [0] * n
    dp[0] = all_boxes[0][2]
    for i in xrange(1,n):
        dp[i] = max([dp[j]+all_boxes[i][2] for j in xrange(i)
                if all_boxes[i][0] > all_boxes[j][0] and 
                all_boxes[i][1] > all_boxes[j][1]]+
                [all_boxes[i][2]])
    return max(dp)


