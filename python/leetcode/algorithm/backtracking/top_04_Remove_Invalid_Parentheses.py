
# 82mins
# dp is better than dfs on performance
def solve(strs):
    n = len(strs)
    if n == 0: return []
    def is_c(s):
        return s != "(" and s != ")"
    dp = [ [ [] for _ in range(n)] for _ in range(n) ]
    for l in range(n):
        for i in range(n-l):
            j = i + l
            if l == 0:
                if is_c(strs[i]):
                    dp[i][j] = [strs[i]]
            elif l == 1:
                if strs[i] == "(" and strs[j] == ")":
                    dp[i][j] = ["()"]
                elif is_c(strs[i]) or is_c(strs[j]):
                    if is_c(strs[i]) and is_c(strs[j]):
                        dp[i][j] = [strs[i:j+1]]
                    elif is_c(strs[i]):
                        dp[i][j] = [strs[i]]
                    else:
                        dp[i][j] = [strs[j]]
            else:
                cur_result = []
                for k in range(i,j):
                    if dp[i][k] and dp[k+1][j]:
                        for l1 in dp[i][k]:
                            for l2 in dp[k+1][j]:
                                if l1 + l2 not in cur_result:
                                    cur_result += l1 + l2,
                    else:
                        cur_result += dp[i][k] + dp[k+1][j]
                if strs[i] == "(" and strs[j] == ")":
                    cur_result += [ strs[i]+ss+strs[j] for ss in dp[i+1][j-1]]
                if cur_result:
                    cur_result.sort(reverse=True, key=len)
                    for ll in cur_result:
                        if len(ll) == len(cur_result[0]):
                            if ll not in dp[i][j]:
                                dp[i][j] += ll,
                        else:
                            break
    # dp.pp()
    return dp[0][-1]

def is_valid(strs):
    left_count = 0
    for c in strs:
        if c == "(":
            left_count += 1
        elif c == ")":
            left_count -= 1
        if left_count < 0:
            return False
    return left_count == 0


def solve(strs):
    n = len(strs)
    if n == 0: return []

    results = []
    queue = [strs]
    visited = {strs:True}
    level = False

    while queue:
        cur = queue.pop(0)
        if is_valid(cur):
            results += cur,
            level = True
        # small than this length of strs will not visit
        if level:
            continue
        for i in range(len(cur)):
            if cur[i] != "(" and cur[i] != ")":
                continue
            new_str = cur[:i] + cur[i+1:]
            if new_str not in visited:
                queue.append(new_str)
                visited[new_str] = True
    return results

def solve(s):
    """
    :type s: str
    :rtype: List[str]
    """
  
    n = len(s)
    if n == 0: return [""]
    dp = [[[] for _ in range(n)] for _ in range(n)]
    def is_valid(ss):
        count = 0
        for c in ss:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0
    for l in range(n):
        for i in range(n-l):
            j = i + l
            # (i,j,s[i:j+1]).p()
            # dp[i][j].p()
            if l == 0:
                if s[i] != "(" and s[i] != ")":
                    dp[i][j] += s[i],
                else:
                    dp[i][j] += "",
            else:
                if is_valid(s[i:j+1]):
                    # s[i:j+1].p()
                    dp[i][j] += s[i:j+1],
                else:
                    max_l = 0
                    if l >= 3 and s[i] == "(" and s[j] == ")":
                        for si in dp[i+1][j-1]:
                            cur_s =  "(" + si + ")"
                            if cur_s not in dp[i][j]:
                                if len(cur_s) > max_l:
                                    dp[i][j] = [cur_s]
                                    max_l = len(cur_s)
                                elif len(cur_s) == max_l:
                                    dp[i][j] += cur_s,
                    # max_l.p()
                    # dp[i][j].p()
                    for k in range(i,j):
                        for si in dp[i][k]:
                            for sj in dp[k+1][j]:
                                cur_s = si + sj
                                if cur_s not in dp[i][j]: 
                                    if len(cur_s) > max_l:
                                        dp[i][j] = [cur_s]
                                        max_l = len(cur_s)
                                    elif len(cur_s) == max_l:
                                        dp[i][j] += cur_s,
            # dp[i][j].p()
    return dp[0][-1]

# this one is from top to bottom, bfs
def solve(s):
    def isvalid(s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr += 1
            elif c == ')':
                ctr -= 1
                if ctr < 0:
                    return False
        return ctr == 0
    level = {s}
    while True:
        valid = filter(isvalid, level)
        if valid:
            return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
if __name__ == '__main__':
    from minitest import *

    with test(is_valid):
        is_valid("()()").must_equal(True)
        is_valid("())()").must_equal(False)
        is_valid("()())()").must_equal(False)

    # with test(solve):
    #     solve("()())()").must_equal(['()()()', '(())()'])
    #     solve("(vc)())()").must_equal(['(vc)()()', '(vc())()'])
    with test(solve):
        solve("()())()").must_equal(['(())()', '()()()'])
        solve("(vc)())()").must_equal(['(vc())()', '(vc)()()'])