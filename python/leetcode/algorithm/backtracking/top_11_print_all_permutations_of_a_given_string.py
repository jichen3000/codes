def solve(the_s):
    n = len(the_s)

    results = []
    def dfs(result):
        if len(result) == n:
            results.append(result)
            return
        nexts = [c for c in the_s if c not in result]
        for c in nexts:
            dfs(result+[c])
    dfs([])
    return results


if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve("abc").pp()