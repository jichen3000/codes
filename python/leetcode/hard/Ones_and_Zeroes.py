from collections import Counter
import itertools

class Solution(object):
    def findMaxForm_not_working(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if len(strs) == 0:
            return 0
        if m <= n:
            less_s = '0'
            larger_s = '1'
            less_sum = m
            larger_sum = n
        else:
            less_s = '1'
            larger_s = '0'
            less_sum = n
            larger_sum = m
        
        # print("less_s,larger_s,less_sum,larger_sum",less_s,larger_s,less_sum,larger_sum)
        count_list = []
        for cur_str in strs:
            cur_counter = Counter(cur_str)
            count_list.append([cur_counter.get(less_s,0),cur_counter.get(larger_s,0)])
        count_list.sort(key=lambda x: x[0]*10000+x[1])
        print("count_list",count_list)

        cur_less_sum = 0
        # less_max_number = 0
        cur_larger_sum = 0
        max_number = 0
        
        for less_v, larger_v in count_list:
            cur_less_sum += less_v
            cur_larger_sum += larger_v
            if cur_less_sum <= less_sum and cur_larger_sum <= larger_sum:
                max_number += 1
            else:
                cur_less_sum -= less_v
                cur_larger_sum -= larger_v

        return max_number
    
    def findMaxForm_brutal(self, strs, m, n):
        if len(strs) == 0:
            return 0
        count_list = []
        for cur_str in strs:
            cur_counter = Counter(cur_str)
            count_list.append([cur_counter.get('0',0),cur_counter.get('1',0)])
        
        def find(count_list,m,n):
            if m < 0 or n < 0: return 0
            if len(count_list) == 0: return 0
            last_m,  last_n = count_list[-1]
            if m >= last_m and n>= last_n:
                return max(find(count_list[0:-1],m,n),
                       1+find(count_list[0:-1],m-last_m,n-last_n))
            else:
                return find(count_list[0:-1],m,n)
        
        return find(count_list, m, n)
    
    def findMaxForm_brutal_2(self, strs, m, n):
        if len(strs) == 0:
            return 0
        count_list = []
        for cur_str in strs:
            cur_counter = Counter(cur_str)
            count_list.append([cur_counter.get('0',0),cur_counter.get('1',0)])
            
        def is_fit(count_list, m, n):
            m_sum, n_sum = 0, 0
            for cur_m, cur_n in count_list:
                m_sum += cur_m
                if m_sum > m:
                    return False
                n_sum += cur_n
                if n_sum > n:
                    return False
            return True
                
        
        for cur_len in xrange(len(strs),0,-1):
            for cur_com in itertools.combinations(count_list, cur_len):
                if is_fit(cur_com, m, n):
                    return cur_len
        return 0
            

            
    def findMaxForm2(self, strs, m, n):
        if len(strs) == 0:
            return 0
        count_list = []
        for cur_str in strs:
            cur_counter = Counter(cur_str)
            count_list.append([cur_counter.get('0',0),cur_counter.get('1',0)])
            
        k_list = [[[0 for _ in xrange(m+1)] for _ in xrange(n+1)] for _ in xrange(len(count_list))]
        for ci in xrange(len(count_list)):
            # if ci > 0:
            mv,nv = count_list[ci]
            for ni in xrange(n+1):
                for mi in xrange(m+1):
                    # if ci==0:
                    #     k_list[0][ni][mi] = 0
                    if nv <= ni and mv <= mi:
                        k_list[ci][ni][mi] = max(1+k_list[ci-1][ni-nv][mi-mv],k_list[ci-1][ni][mi])
                    else:
                        k_list[ci][ni][mi] = k_list[ci-1][ni][mi]
                    # if ci > 0:
                    #     print("ci,ni,mi,k_list[ci][ni][mi],nv,mv",ci,ni,mi,k_list[ci][ni][mi],nv,mv)
                    # else:
                    #     print("ci,ni,mi,k_list[ci][ni][mi]",ci,ni,mi,k_list[ci][ni][mi])


        return k_list[len(count_list)-1][n][m]

    def findMaxForm_complex(self, strs, m, n):
        if len(strs) == 0:
            return 0
        count_list = []
        for cur_str in strs:
            cur_counter = Counter(cur_str)
            count_list.append([cur_counter.get('0',0),cur_counter.get('1',0)])
            
        k_list = [[[0 for _ in xrange(m+1)] for _ in xrange(n+1)] for _ in xrange(len(count_list)+1)]
        for ci in xrange(len(count_list)+1):
            if ci > 0:
                mv,nv = count_list[ci-1]
            for ni in xrange(n+1):
                for mi in xrange(m+1):
                    if ci==0:
                        k_list[0][ni][mi] = 0
                    elif nv <= ni and mv <= mi:
                        k_list[ci][ni][mi] = max(1+k_list[ci-1][ni-nv][mi-mv],k_list[ci-1][ni][mi])
                    else:
                        k_list[ci][ni][mi] = k_list[ci-1][ni][mi]
                    # if ci > 0:
                    #     print("ci,ni,mi,k_list[ci][ni][mi],nv,mv",ci,ni,mi,k_list[ci][ni][mi],nv,mv)
                    # else:
                    #     print("ci,ni,mi,k_list[ci][ni][mi]",ci,ni,mi,k_list[ci][ni][mi])


        return k_list[len(count_list)][n][m]

    def findMaxForm(self, strs, m, n):
        '''
            compare the combination 2 ** len(strs), 
            save a lot of time, now is m * n * len(strs)
        '''
        if len(strs) == 0:
            return 0
        count_list = []
        for cur_str in strs:
            cur_counter = Counter(cur_str)
            count_list.append([cur_counter.get('0',0),cur_counter.get('1',0)])

        k_list = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for mv, nv in count_list:
            # mi,ni start from big, this is most important
            for mi in xrange(m, -1, -1):
                for ni in xrange(n, -1, -1):
                    print("mv,nv,mi,ni",mv, nv,mi,ni)
                    if nv <= ni and mv <= mi:
                        k_list[mi][ni] = max(
                            1+k_list[mi-mv][ni-nv],k_list[mi][ni])
                        print("k[{}][{}]=max(1+k[{}][{}] ({}),k[{}][{}] ({}))".format(
                            mi,ni,mi-mv,ni-nv,1+k_list[mi-mv][ni-nv],mi,ni,k_list[mi][ni]),k_list[mi][ni])
        k_list.pp()
        return k_list[m][n]
     
    # def findMaxForm(self, strs, m, n):
        
    #     dp = [[0] * (n+1) for _ in range(m+1)]
        
    #     def count(s):
    #         return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        
    #     for z, o in [count(s) for s in strs]:
    #         for x in range(m, -1, -1):
    #             for y in range(n, -1, -1):
    #                 if x >= z and y >= o:
    #                     dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])
                        
    #     return dp[m][n]

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # strs = ["10","1","0"]
        # Solution().findMaxForm(strs,1,1).p()            
        strs = ["10","0001","11001","1","0"]
        Solution().findMaxForm(strs,5,3).p()            
        # strs = ["00101011"]
        # Solution().findMaxForm(strs,36,39).p()            
        
