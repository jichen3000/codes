
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = ("+","-","*","/")
        stack = []
        for t in tokens:
            if t in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if "." not in operand1:
                    operand1 += ".0"
                v = eval(operand1+t+operand2)
                # (operand1+t+operand2,v).p()
                stack += str(int(v)),
            else:
                stack += t,
        # return int(round(float(stack.pop())))
        return int(stack.pop())
        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().evalRPN(["0","3","/"]).must_equal(0)
        # Solution().evalRPN(["2","1","+","3","*"]).must_equal(9)
        Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]).must_equal(22)
        Solution().evalRPN(["4","13","5","/","+"]).must_equal(6)
