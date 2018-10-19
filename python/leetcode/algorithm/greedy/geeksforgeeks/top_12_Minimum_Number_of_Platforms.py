def solve(arrs, deps):
    if len(arrs) == 0: return 0
    all_times = zip(arrs, deps)
    all_times.sort(key=lambda l:l[1])
    arr, dep = all_times.pop(0)
    platforms = [dep]
    for arr, dep in all_times:
        for i in range(len(platforms)):
            if arr > platforms[i]:
                platforms[i] = dep
                break
        else:
            platforms += dep,
    return len(platforms)

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        arr = [900, 940, 950, 1100, 1500, 1800]
        dep = [910, 1200, 1120, 1130, 1900, 2000]
        solve(arr,dep).must_equal(3)

