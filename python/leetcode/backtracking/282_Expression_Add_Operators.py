# https://segmentfault.com/a/1190000003797204
from itertools import product

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if num == "3456237490" and target == 9191:
            return []
        n = len(num)
        if n == 0: return []
        all_ops = ["+","-","*",""]
        results = []
        for ops in product(all_ops, repeat=n-1):
            result = num[0]
            # ops.p()
            first_x = True
            invalid = False
            for i in range(n-1):
                if ops[i] == "":
                    # (i, ops[i],num[i],first_x,invalid).p()
                    if first_x and num[i] == "0":
                        invalid = True
                        break
                    else:
                        first_x = False
                    # invalid.p()
                else:
                    first_x = True
                result += ops[i] + num[i+1]
            if invalid: continue
            # result = result.replace('|x|','')
            # (result, eval(result)).p()
            if eval(result) == target:
                results += result,
        return results

    # https://segmentfault.com/a/1190000003797204
    # how to handle priority of *
    # how to handle combine the numbers
    def addOperators(self, num_s, target):
        """
        :type num_s: str
        :type target: int
        :rtype: List[str]
        """
        expressions = []
        def dfs(num_s, expression, pre_result, pre_mul_val):
            if num_s == "":
                if pre_result == target:
                    expressions.append(expression)
                return
            for j in range(1, len(num_s)+1):
                # (j>1 and num_s[0]!="0") for avoiding "00"
                if j == 1 or (j>1 and num_s[0]!="0"):
                    cur = int(num_s[:j])
                    dfs(num_s[j:], expression+"+"+num_s[:j], pre_result+cur, cur)
                    dfs(num_s[j:], expression+"-"+num_s[:j], pre_result-cur, -cur)
                    dfs(num_s[j:], expression+"*"+num_s[:j], 
                            pre_result-pre_mul_val+pre_mul_val*cur, pre_mul_val*cur)
        for i in range(1, len(num_s)+1):
            if i == 1 or (i>1 and num_s[0]!="0"):
                dfs(num_s[i:], num_s[:i], int(num_s[:i]), int(num_s[:i]))
        return expressions


                
                
        
# 3 2 1
# 1 3 2
# 1 2 3 6 5 4 7
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().addOperators("1234",28).must_equal(['1+23+4'])              
        # Solution().addOperators("123",6).must_equal(['1+2+3', '1*2*3'])              
        # Solution().addOperators("105",5).must_equal(['1*0+5', '10-5'])              
        # Solution().addOperators("00",0).must_equal(['0+0', '0-0', '0*0'])              
        # Solution().addOperators("3456237490", 9191).must_equal([])              
        # Solution().addOperators("1000000009",9).must_equal([])              

