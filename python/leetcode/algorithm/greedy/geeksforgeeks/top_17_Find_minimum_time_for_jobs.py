# http://www.geeksforgeeks.org/find-minimum-time-to-finish-all-jobs-with-given-constraints/
def solve(jobs, assignee_count):
    end_units = sum(jobs)
    start_units = max(jobs)
    def is_possible(time_units):
        cur_count = 0
        cur_sum = 0
        for units in jobs:
            if cur_sum + units > time_units:
                cur_count += 1
                cur_sum = units
            elif cur_sum + units == time_units:
                cur_count += 1
                cur_sum = 0
            else:
                cur_sum += units
        return cur_count <= assignee_count
    answer = end_units
    while start_units <= end_units:
        mid_units = (start_units + end_units)/2
        if is_possible(mid_units):
            end_units = mid_units - 1
            answer = mid_units
        else:
            start_units = mid_units + 1
    return answer

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        jobs = [10, 7, 8, 12, 6, 8]
        solve(jobs, 4).must_equal(15)
        
