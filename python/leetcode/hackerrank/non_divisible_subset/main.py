
def main(n, k, s_list):
    if k == 1: return 1
    remain_dict = {i:0 for i in range(k)}
    max_len = 0
    for i in s_list:
        remain = i % k
        remain_dict[remain] += 1

    max_set_size = (k-1)/2
    pair_list = [(i+1, k-i-1) for i in range(max_set_size)]
    for i, ni in pair_list:
        # print(i,ni)
        # print(max(remain_dict[i], remain_dict[ni]))
        max_len += max(remain_dict[i], remain_dict[ni])

    
    addtional = 0
    if k % 2 == 0 and remain_dict[k/2]>0:
        remain_dict[k/2] = 0
        addtional += 1
    if remain_dict[0]>0:
        addtional += 1
        remain_dict[0] = 0
    # print(len(remain_dict))
    # print(remain_dict.keys())
    # print(remain_dict)

    max_len += addtional

    return max_len

if __name__ == '__main__':
    # from minitest import *

    # with test(main):
    #     main(10,4,range(1,11)).must_equal(5)
        # main(5,1,range(1,6)).must_equal(1)

    # cat test14.txt | python main.py , result = 2
    # cat test9.txt | python main.py , result = 49747
    n, k = map(int, raw_input().strip().split(" "))
    s_list = map(int, raw_input().strip().split(" "))
    print(main(n,k,s_list)) 

