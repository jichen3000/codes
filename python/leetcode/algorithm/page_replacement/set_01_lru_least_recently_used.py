def solve(pages, capacity):
    '''
        return count of page fault
    '''
    count = 0
    cache = {}
    for i in range(len(pages)):
        cur = pages[i]
        # (i,cur).p()
        if cur not in cache:
            count += 1
            # count.p()
            if len(cache) >= capacity:
                min_index = len(pages)
                replace_v = -1
                for k, v in cache.items():
                    if v < min_index:
                        min_index = v
                        replace_v = k
                del cache[replace_v]

        cache[cur] = i
        # cache.p()
    return count

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
        solve(pages,4).must_equal(6)