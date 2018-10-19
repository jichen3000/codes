def solve(jobs):
    results = []
    def compare1(j1, j2):
        if j1[1] != j2[1]:
            return cmp(j1[1],j2[1])
        else:
            return cmp(j1[2],j2[2])
    jobs.sort(cmp=compare1, reverse=True)
    # jobs.p()
    title, deadline, value = jobs.pop(0)
    dead_index = deadline
    while dead_index > 0:
        results += title,
        title, deadline, value = jobs.pop(0)
        if dead_index <= deadline:
            dead_index -= 1
        else:
            dead_index = deadline
    return list(reversed(results))

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        jobs = [ ['a', 2, 100], ['b', 1, 19], ['c', 2, 27],
                   ['d', 1, 25], ['e', 3, 15]]
        solve(jobs).must_equal(['c', 'a', 'e'])
            