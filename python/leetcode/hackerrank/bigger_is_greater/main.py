def find_smallest_big(the_str):
    for i in range(len(the_str)-2,-1,-1):
        smallest_index = None
        for j in range(i+1, len(the_str)):
            if the_str[i] < the_str[j]:
                if smallest_index:
                    if the_str[smallest_index] > the_str[j]:
                        smallest_index = j
                else:
                    smallest_index = j
        if smallest_index:
            new_one = list(the_str)
            smallest_index.p()
            i.p()
            new_one[i],new_one[smallest_index] = new_one[smallest_index],new_one[i]
            # if i > 0:
            new_one = new_one[0:i+1] + sorted(new_one[i+1:])
            # else:
            #     new_one = [new_one[0]] + sorted(new_one[i+1:])
            return "".join(new_one)
    return "no answer"

# n = int(raw_input().strip())
# for i in xrange(n):
#     the_str = raw_input().strip()
#     print(find_smallest_big(the_str))


if __name__ == '__main__':
    from minitest import *

    with test(find_smallest_big):
        find_smallest_big("ab").must_equal("ba")
        find_smallest_big("bb").must_equal("no answer")
        find_smallest_big("hefg").must_equal("hegf")
        find_smallest_big("dkhc").must_equal("hcdk")