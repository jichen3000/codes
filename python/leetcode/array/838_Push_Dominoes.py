class Solution:
    def pushDominoes(self, s):
        """
        :type dominoes: str
        :rtype: str
        """
        if not s: return s
        n = len(s)
        if n <= 1: return s
        s = list(s)
        while True:
            count = 0
            temp = s[::]
            for i in range(n):
                if s[i] == ".":
                    if i == 0:
                        if s[i+1] == "L":
                            temp[i] = "L"
                            count += 1
                    elif i == n - 1:
                        if s[i-1] == "R":
                            temp[i] = "R"
                            count += 1
                    else:
                        if s[i-1] == "R" and s[i+1] == "L":
                            pass
                        elif s[i-1] == "R":
                            temp[i] = "R"
                            count += 1
                        elif s[i+1] == "L":
                            temp[i] = "L"
                            count += 1
            if count == 0:
                break
            s = temp
        return "".join(s)