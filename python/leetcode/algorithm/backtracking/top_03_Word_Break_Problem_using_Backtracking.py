def solve(dictionary, the_s):
    sn = len(the_s)
    if sn == 0: return []
    if len(dictionary) == 0: return []
    def inner(the_s):
        n = len(the_s)
        results = []
        for i in range(n):
            if the_s[:i+1] in dictionary:
                if i == n-1:
                    results += the_s,
                else:
                    results += [the_s[:i+1] + " " +l 
                            for l in inner(the_s[i+1:]) if len(l)>0]
        return results
    return inner(the_s)


if __name__ == '__main__':
    from minitest import *

    with test(solve):
        dictionary = ["lee","leet","code"] 
        solve(dictionary, "leetcode").must_equal(['leet code'])
        dictionary = ["mobile","samsung","sam","sung",
                            "man","mango", "icecream","and",
                            "go","i","love","ice","cream"] 
        solve(dictionary, "iloveicecreamandmango").must_equal([
                'i love ice cream and man go', 
                'i love ice cream and mango', 
                'i love icecream and man go', 
                'i love icecream and mango'])


