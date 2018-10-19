# Smallest Substring of All Characters

# big O is m + n
def get_shortest_unique_substring(arr, s):
    n = len(s)
    an = len(arr)
    if an > n: return ""
    head = 0
    while head < n and s[head] not in arr:
        head += 1

    if head == n: return ""
    if an == 1: return s[head]

    mem = {}
    min_len = n + 1
    min_s = ""
    tail = head
    while tail < n:
        if s[tail] in arr:
            mem[s[tail]] = mem.get(s[tail], 0) + 1
            if len(mem) == an:
                while len(mem) == an:
                    if tail + 1 - head  < min_len:
                        min_len = tail + 1 - head
                        min_s = s[head:tail+1]
                        if min_len == an:
                            return min_s
                    if s[head] in mem:
                        mem[s[head]] -= 1
                        if mem[s[head]] == 0:
                            del mem[s[head]]

                    head += 1

        tail += 1
    return min_s

# big O is m * n
def get_shortest_unique_substring(arr, s):
    mem = {}
    for c in arr:
        mem[c] = None
    n = len(s)
    def get_range():
        start, end = n, -1
        for k, v in mem.items():
            if v!=None:
                start = min(start, v)
                end = max(end, v)
            else:
                return [None, None]
        return [start, end]
    min_len = n + 1
    min_s = ""
    for i,c in enumerate(s):
        if c in mem:
            mem[c] = i
            start, end = get_range()
            # (i,start, end, mem).p()
            if start!=None and end + 1 - start < min_len:
                min_len = end + 1 - start
                min_s = s[start: end+1]
    return min_s

if __name__ == '__main__':
    from minitest import *

    with test(get_shortest_unique_substring):
        get_shortest_unique_substring(["x"], "y").must_equal("")
        get_shortest_unique_substring(["x"], "").must_equal("")
        get_shortest_unique_substring(["x"], "x").must_equal("x")
        get_shortest_unique_substring(["x"], "yx").must_equal("x")
        get_shortest_unique_substring(["x","y","z"], "xyyzyzyx").must_equal("zyx")
        get_shortest_unique_substring(["x","y","z"], "xyayzybzyx").must_equal("zyx")
        get_shortest_unique_substring(["A","B","C"], "ADOBECODEBANCDDD").must_equal("BANC")

