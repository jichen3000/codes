## observe:
## first it can be handle by dfs
##            5
##     /      |       \
##    4       3        2 
##    |\     / \      /| 
##    2 1   2   0    1 0
## every level means get a weight.
## so time: O(n!)
## base case left_weight == 0
## recursion rule: get a weight
def solve(weights, values, total_weight):
    '''
        recursion_dfs
    '''
    max_value = [0]
    n = len(weights)
    indexes = list(range(n))
    def dfs(index, left_weight, cur_value):
        if index >= n or left_weight == 0:
            max_value[0] = max(max_value[0], cur_value)
            return
        for i in range(index, n):
            real_i = indexes[i]
            w, v = weights[real_i], values[real_i]
            if w <= left_weight:
                indexes[i], indexes[index] = indexes[index], indexes[i]
                dfs(index + 1, left_weight - w, cur_value + v)
                indexes[i], indexes[index] = indexes[index], indexes[i]
    dfs(0, total_weight, 0)
    return max_value[0]

## dp
## generated rule: have a max limitation, find another max or min value
## dp[i][j], i means weight, j means one of type, dp means max value in this weight
## base case: j = 0
## dp[i][j] for j in range(n):  cur = dp[i - weights[j]][j-1] + values[j]
## which loop outside? this dependens on case.
##   in this case, using types as outside is quite simple.
##   why using reversing loop for weight, since if not, it would put one thing multiple times.
def solve(weights, values, total_weight):
    '''
        dp
    '''
    max_value = [0]
    n = len(weights)
    dp = [0] * (total_weight + 1)
    for j in range(n):
        for w in range(total_weight, weights[j] - 1, -1):
            dp[w] = max(dp[w - weights[j]] + values[j], dp[w])
        # dp.p()
    return dp[-1]
# # # cannot be reduce to one array, since you cannot get dp[i-1][j-weights[i]],
# # # it will become dp[i][j-weights[i]], and the result will be not 0-1 knapsack
# # # it become one item can be choosen many times.
# def solve(weights, values, total_weight):
#     n = len(weights)
#     if n == 0: return 0
#     dp = [[0] * (total_weight+1) for _ in range(n)]
#     for i in range(n):
#         for j in range(total_weight+1):
#             if i == 0 and j >= weights[i]:
#                 dp[i][j] = values[i]
#             else:
#                 if j >= weights[i]:
#                     dp[i][j] = max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])
#                 else:
#                     dp[i][j] = dp[i-1][j]
#     # dp.pp()
#     return dp[-1][-1]



if __name__ == '__main__':
    from minitest import *

    with test(solve):
        # solve((1,2,3),(60,100,120),5).must_equal(220)
        # solve((1,2,3),(60,100,120),6).must_equal(280)
        solve((1,2,3,4,5),(60,100,120, 150, 180), 10).must_equal(430)
        