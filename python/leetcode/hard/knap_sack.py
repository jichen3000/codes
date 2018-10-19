#A naive recursive implementation of 0-1 Knapsack Problem
 
# Returns the maximum value that can be put in a knapsack of
# capacity W
def knapSack_brutal(W , wt , val , n):
 
    # Base Case
    if n == 0 or W == 0 :
        return 0
 
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
                   knapSack(W , wt , val , n-1))
 
# end of function knapSack
 
def knapSack_origin(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
            (i,w,K[i][w],wt[i-1],val[i-1]).p()
 
    return K[n][W]

def knapSack(W, wt, val, n):
    K = [0 for x in range(W+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n):
        for w in range(W,-1,-1):
            if w==0:
                K[w] = 0
            elif wt[i] <= w:
                K[w] = max(val[i] + K[w-wt[i]],  K[w])
            # else:
            #     K[i][w] = K[i-1][w]
            # (i,w,K[i][w],wt[i-1],val[i-1]).p()
 
    return K[W]

def knapSack(weight_limit, weights, values, n):
    dp = [0] * (weight_limit + 1)
    for i in range(len(weights)):
        for weight in range(weight_limit, weights[i]-1, -1):
            dp[weight] = max(values[i] + dp[weight - weights[i]], dp[weight])
    return dp[-1]

# This code is contributed by Nikhil Kumar Singh


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

if __name__ == '__main__':
    from minitest import *

    with test(knapSack):
        val = [60, 100, 120]
        wt = [10, 20, 30]
        W = 50
        n = len(val)
        # knapSack(W , wt , val , n).p()
        knapSack(W , wt , val , n).must_equal(220)
        knapSack(10, (1,2,3,4,5),(60,100,120, 150, 180), 5).p()