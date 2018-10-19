class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        for line in logs:
            fid, action, time = line.split(":")
            fid, time= int(fid), int(time)
            if action =="start":
                if stack:
                    stack[-1][1] += time-stack[-1][0]
                stack += [time, 0],
            else:
                start_time, pass_time = stack.pop()
                res[fid] += time + 1 - start_time + pass_time
                if stack:
                    stack[-1][0] = time + 1
        return res
            
class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        for line in logs:
            id, op, time = line.split(":")
            id, time = int(id), int(time)
            # print(id, op, time)
            if op == "start":
                if stack:
                    res[stack[-1][0]] += time - stack[-1][1] -1
                    stack[-1][1] += time - stack[-1][1]
                stack += [id, time],
            else:
                pre_id, pre_time = stack.pop()
                res[pre_id] += time - pre_time + 1
                if stack:
                    stack[-1][1] = time
            # print(stack, res)
        return res        