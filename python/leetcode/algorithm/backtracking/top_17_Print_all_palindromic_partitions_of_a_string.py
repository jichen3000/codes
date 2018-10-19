def solve(the_s):
    n = len(the_s)
    group_count = 2 ^ n - 1
    groups = []
    def is_p(ss):
        n = len(ss)
        if n == 0: return False
        for i in range(n/2):
            if ss[i] != ss[n-1-i]:
                return False
        return True


    def dfs(group, index):
        if index == n:
            # group.p()
            groups.append(group[:])
            return 

        pre = group[-1]
        if is_p(group[-1] + the_s[index]):
            group[-1] += the_s[index]
            dfs(group, index+1)
            group[-1] = pre

        group.append(the_s[index])
        dfs(group, index+1)
        group.pop()
    dfs([the_s[0]],1)
    return groups

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve("geeks").pp()
