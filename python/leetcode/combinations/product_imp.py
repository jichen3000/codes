def product(list_list):
    if not list_list: return []
    n = len(list_list)
    ilist = [0] * n
    res = []
    while True:
        res += [list_list[i][ilist[i]] for i in range(n)],
        i = n - 1
        ilist[i] += 1
        while i>=0 and ilist[i] == len(list_list[i]):
            ilist[i] = 0
            i -= 1
            ilist[i] += 1
        if i < 0: break
    return res


def product_generator(list_list):
    if not list_list: return None
    n = len(list_list)
    ilist = [0] * n
    while True:
        yield [list_list[i][ilist[i]] for i in range(n)]
        i = n - 1
        ilist[i] += 1
        while i>=0 and ilist[i] == len(list_list[i]):
            ilist[i] = 0
            i -= 1
            ilist[i] += 1
        if i < 0: break

    
if __name__ == '__main__':
    from minitest import *

    with test(product):
        product(["abc","ed","mn"]).must_equal([
                ['a', 'e', 'm'],
                ['a', 'e', 'n'],
                ['a', 'd', 'm'],
                ['a', 'd', 'n'],
                ['b', 'e', 'm'],
                ['b', 'e', 'n'],
                ['b', 'd', 'm'],
                ['b', 'd', 'n'],
                ['c', 'e', 'm'],
                ['c', 'e', 'n'],
                ['c', 'd', 'm'],
                ['c', 'd', 'n']])
    with test(product_generator):
        for l in product_generator(["abc","ed","mn"]):
            l.p()