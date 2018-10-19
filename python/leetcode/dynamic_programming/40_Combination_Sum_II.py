class Solution(object):
    def combinationSum2_dp_top_down(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]] 30mins
        """ 
        def c(i,target):
            print("i,target",i,target)
            if i == 0:
                if target == candidates[i]:
                    return [[candidates[i]]]
                else:
                    return []
            else:
                if candidates[i] > target:
                    return c(i-1, target)
                elif candidates[i] == target:
                    return [[candidates[i]]] + c(i-1, target)
                else:
                    results = c(i-1,target-candidates[i]) 
                    print("results",results)
                    return [l+[candidates[i]] for l in results] + c(i-1, target)
        return c(len(candidates)-1,target)
    
    def combinationSum2_matrix(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]] 30mins
        """ 
        nums.sort()
        n = len(nums)
        dp = [[ [] for j in xrange(target+1) ] for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(1, target+1):
                if i == 0:
                    # print("i,j,nums[i]",i,j,nums[i])
                    if j == nums[i]:
                        dp[i][j] = [[nums[i]]]
                else:
                    if j < nums[i]:
                        dp[i][j] = dp[i-1][j]
                    elif j == nums[i]:
                        # print("dp[i-1][j]",dp[i-1][j-nums[i]])
                        dp[i][j] = dp[i-1][j] + [[nums[i]]]
                    else:
                        for l in dp[i-1][j-nums[i]]:
                            # print("l + [nums[i]]",l + [nums[i]])
                            dp[i][j] += l + [nums[i]],
                        dp[i][j] += dp[i-1][j]
                    # print("i,j,nums[i],dp[i][j]",i,j,nums[i],dp[i][j])
        # print("dp:",dp)
        result = []
        for i in xrange(n):
            for l in dp[i][target]:
                if l not in result:
                    result += l,
        return result

    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]] 30mins
        """
        nums.sort()
        n = len(nums)
        dp = [ [] for j in xrange(target+1) ]
        for i in xrange(n):
            for j in xrange(target, 0, -1):
                if i == 0:
                    # print("i,j,nums[i]",i,j,nums[i])
                    if j == nums[i]:
                        dp[j] = [[nums[i]]]
                else:
                    if j > nums[i]:
                        for l in dp[j-nums[i]]:
                            # print("l + [nums[i]]",l + [nums[i]])
                            cur = l + [nums[i]]
                            if cur not in dp[j]:
                                dp[j] += cur,
                    elif j == nums[i]:
                        # print("dp[i-1][j]",dp[i-1][j-nums[i]])
                        if [nums[i]] not in dp[j]:
                            dp[j] += [nums[i]],

        return dp[target]



            
                                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().combinationSum2([10,1,2,7,6,1,5],8).must_equal(
                [[1,2,5],[1,7],[1,1,6],[2,6]])