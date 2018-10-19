# https://leetcode.com/contest/weekly-contest-93/problems/minimum-number-of-refueling-stops/

class Solution:
    def minRefuelStops(self, target, start_fuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        n = len(stations)
        if start_fuel >= target: return 0

        def dfs(i, start, fuel, count):
            # (i, start, fuel, count).p()
            nexts = [float("inf")]
            for j in range(i+1, n):
                s, f = stations[j]
                # (i,j,s,f, fuel >= s - start, f + fuel >= target-start).p()
                if fuel >= s - start:
                    if f + fuel >= target-start:
                        # (count + 1).p()
                        return count + 1
                    nexts += dfs(j, s, fuel - (s - start) + f, count + 1),
                else:
                    # "break".p()
                    break
            # min(nexts).p()
            return min(nexts)

        res = dfs(-1, 0, start_fuel, 0)
        # res.p()
        if res == float("inf"):
            return -1
        return res
        
    # dp[t] means the furthest distance that we can get with t times of refueling.

    # So for every station s[i],
    # if the current distance dp[t] >= s[i][0], we can refuel:
    # dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])

    # In the end, we'll return the first t with dp[i] >= target,
    # otherwise we'll return -1.

    # Time Complexity:
    # O(N^2)
    def minRefuelStops(self, target, start_fuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        n = len(stations)
        dp = [start_fuel] + [0] * n
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().minRefuelStops(1,1,[]).must_equal(0)
        # Solution().minRefuelStops(100,1,[[10,50]]).must_equal(-1)
        # Solution().minRefuelStops(100,10,[[10,60],[20,20],[30,20],[60,40]]).must_equal(2)
        # Solution().minRefuelStops(100,50,[[40,50]]).must_equal(1)
        # Solution().minRefuelStops(100,25,[[25,25],[50,25],[75,25]]).must_equal(3)
        # Solution().minRefuelStops(1000,70,
        #         [[53,170],[144,184],[285,250],[551,63],[563,183],[652,16],[720,328],[821,7],[941,180],[978,58]]
        #         ).must_equal(5)
        # Solution().minRefuelStops(1000000000,
        #         145267354,
        #         [[5510987,84329695],[10682248,76273791],[56227783,136858069],[91710087,18854476],[111148380,127134059],[165982642,122930004],[184216180,124802819],[217578071,7123113],[233719001,95862544],[339631786,7676497],[349762649,136128214],[403119403,21487501],[423890164,61095325],[424072629,50415446],[572994480,13561367],[609623597,69207102],[662818314,84432133],[678679727,20403175],[682325369,14288077],[702137485,6426204],[716318901,47662322],[738137702,129579140],[761962118,23765733],[820353983,70497719],[895811889,75533360]]
        #         ).must_equal(9)
        # Solution().minRefuelStops(1000,
        #         299,
        #         [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]
        #         ).must_equal(4)
        # Solution().minRefuelStops(1000,
        #         299,
        #         [[14,123],[145,203],[344,26],[357,68],[390,35],[478,135],[685,108],[823,186],[934,217],[959,80]]
        #         ).must_equal(5)
        Solution().minRefuelStops(20,
                2,
                [[2,6],[4,1],[8,3],[9,20],[10,3],[12,10]]
                ).must_equal(5)
