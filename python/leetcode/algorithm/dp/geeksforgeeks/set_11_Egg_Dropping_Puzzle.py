def solve(eggs_count, floor_count):
    if floor_count == 1 or floor_count == 0:
        return floor_count
    if eggs_count == 1:
        return floor_count
    # solve(eggs_count-1, i-1) means egg breaks on i th floor
    # solve(eggs_count, floor_count-i) means egg does not break
    # max means get the worst case
    return 1 + min(max(
            solve(eggs_count-1, i-1),
            solve(eggs_count, floor_count-i)) 
                for i in range(1, floor_count+1))

def solve(eggs_count, floor_count):  
    if floor_count == 1 or floor_count == 0:
        return floor_count
    if eggs_count == 1:
        return floor_count
    dp = [ [0]*(floor_count+1) for _ in xrange(eggs_count+1)]
    for i in xrange(1, eggs_count+1):
        for j in xrange(1, floor_count+1):
            if i==1 or j==1:
                dp[i][j] = j
            else:
                dp[i][j] = 1+min(max(dp[i-1][k-1],dp[i][j-k]) 
                        for k in xrange(1,j+1))
    dp.p()
    return dp[-1][-1]
# def solve(eggs_count, floor_count):  
#     if floor_count == 1 or floor_count == 0:
#         return floor_count
#     if eggs_count == 1:
#         return floor_count
#     dp = [0]*(floor_count+1)
#     for i in xrange(1, eggs_count+1):
#         for j in xrange(1, floor_count+1):
#             pre_dp = dp[:]
#             if i==1 or j==1:
#                 dp[j] = j
#             else:
#                 dp[j] = 1+min(max(pre_dp[k-1],dp[j-k]) 
#                         for k in xrange(1,j+1))
#     # dp.p()
#     return dp[-1]
if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve(3,14).must_equal(4)
        solve(3,36).must_equal(6)