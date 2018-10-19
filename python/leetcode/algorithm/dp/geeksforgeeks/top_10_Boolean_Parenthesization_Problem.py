
def solve(symbols_str, operators_str):
    symbols = list(symbols_str)
    operators = list(operators_str)
    n = len(symbols)
    dp_true = [[0] * n for _ in xrange(n)]
    dp_false = [[0] * n for _ in xrange(n)]
    for l in xrange(0,n):
        for i in xrange(n-l):
            j = i + l
            if l == 0:
                if symbols[i] == "T":
                    dp_true[i][j] = 1
                    dp_false[i][j] = 0
                else:
                    dp_true[i][j] = 0
                    dp_false[i][j] = 1
            else:
                for k in xrange(i,j):
                    if operators[k] == "&":
                        dp_true[i][j] += dp_true[i][k] * dp_true[k+1][j]
                        dp_false[i][j] += (dp_true[i][k]+dp_false[i][k]) * (dp_true[k+1][j]+dp_false[k+1][j]) - \
                                dp_true[i][k] * dp_true[k+1][j]
                    elif operators[k] == "|":
                        dp_false[i][j] += dp_false[i][k] * dp_false[k+1][j]
                        dp_true[i][j] += (dp_true[i][k]+dp_false[i][k]) * (dp_true[k+1][j]+dp_false[k+1][j]) - \
                                dp_false[i][k] * dp_false[k+1][j]
                    elif operators[k] == "^":
                        dp_true[i][j] += dp_true[i][k] * dp_false[k+1][j] + dp_false[i][k] * dp_true[k+1][j]
                        dp_false[i][j] += dp_true[i][k] * dp_true[k+1][j] + dp_false[i][k] * dp_false[k+1][j]
    return dp_true[0][-1]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve("TTFT", "|&^").must_equal()
