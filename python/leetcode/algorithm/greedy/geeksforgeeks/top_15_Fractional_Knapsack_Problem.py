def solve(items, total):
    if total == 0: return 0
    if len(items) == 0: return 0
    rate_weights = [(float(value) / weight, value, weight) for value, weight in items]
    rate_weights.sort(reverse=True)
    cur_weights, cur_values = 0, 0
    for rate, value, weight in rate_weights:
        if weight + cur_weights < total:
            cur_weights += weight
            cur_values += value
        else:
            left_weight = total - cur_weights
            cur_values += left_weight * rate
            cur_weights = total
        if cur_weights == total:
            break
    return int(cur_values)


if __name__ == '__main__':
    from minitest import *

    with test(solve):
        # value, weight
        items = [[100, 20],[60, 10],  [120, 30]]
        solve(items, 50).must_equal(240)
