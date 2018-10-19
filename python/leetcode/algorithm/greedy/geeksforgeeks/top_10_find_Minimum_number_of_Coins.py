def solve(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    coins.sort(reverse=True)
    cur_v = target
    results = []
    for coin in coins:
        if coin <= cur_v:
            div_v = cur_v / coin
            results += [coin]*div_v
            cur_v -= coin * div_v
            if cur_v == 0: break
    return len(results)

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve(70).must_equal(2)
        solve(121).must_equal(3)
        solve(126).must_equal(4)
        solve(93).must_equal(5)
