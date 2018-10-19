def merge_two_sorted(la,lb):
    # if len(la) == 0:
    #     return lb
    # if len(lb) == 0:
    #     return la
    i, j= 0,0
    result = []
    while i<len(la) and j <len(lb):
        if la[i] <= lb[j]:
            result.append(la[i])
            i += 1
        else:
            result.append(lb[j])
            j += 1
    for left_i in xrange(i,len(la)):
        result.append(la[left_i])
    for left_j in xrange(j,len(lb)):
        result.append(lb[left_j])
    return result

def merge_sort(the_list):
    n = len(the_list)
    if n <= 1:
        return the_list
    left_list = merge_sort(the_list[:n/2])
    right_list = merge_sort(the_list[n/2:])
    return merge_two_sorted(left_list, right_list)

# not fully inplace
# O(n log n), Ο(n)
def merge_sort_inplace(the_list):
    n = len(the_list)
    if n <= 1:
        return the_list
    def merge_in(left,right):
        if right - left <=1: return
        mid = (left+right) / 2
        merge_in(left, mid)
        merge_in(mid, right)
        sorted_list = [] # length will be right - left
        right_i = mid
        for i in range(left, mid):
            while right_i < right and the_list[right_i] < the_list[i]:
                sorted_list += the_list[right_i],
                right_i += 1
            sorted_list += the_list[i],
        for i in range(left, right_i):
            the_list[i] = sorted_list[i-left]

    merge_in(0,n)
    return the_list

def merge_sort_inplace(arr):
    """
    :type arr: List[int]
    :rtype: None
    replace in place

    time: O(n log n), space: O(n)
    """
    def merge_sorted_lists(arr1, arr2):
        res = []
        i = j = 0
        while i < len(arr1) or j < len(arr2):
            if i >= len(arr1):
                res += arr2[j],
                j += 1
            elif j >= len(arr2):
                res += arr1[i],
                i += 1
            else:
                if arr1[i] > arr2[j]:
                    res += arr2[j],
                    j += 1
                else:
                    res += arr1[i],
                    i += 1
        return res

        # while arr1 or arr2:
        #     if not arr1:
        #         res += arr2.pop(0),
        #     elif not arr2:
        #         res += arr1.pop(0),
        #     else: # arr1 and arr2 not empty
        #         v = arr1.pop(0) if arr1[0] < arr2[0] else arr2.pop(0)
        #         res += v,
        # return res

    def helper(l, r):
        if l + 1 == r:
            return arr[l:r]
        m = (l + r + 1)//2
        l_arr = helper(l, m)
        r_arr = helper(m, r)
        return merge_sorted_lists(l_arr, r_arr)

    return helper(0, len(arr))

if __name__ == '__main__':
    from minitest import *

    # with test(merge_two_sorted):
    #     la = [1,3,5,7,9]
    #     lb = [2,4,6]
    #     merge_two_sorted(la,lb).must_equal(
    #             [1, 2, 3, 4, 5, 6, 7, 9])

    # with test(merge_sort):
    #     merge_sort([4,3,5,7,8,2,1]).must_equal(
    #             [1, 2, 3, 4, 5, 7, 8])

    with test(merge_sort_inplace):
        merge_sort_inplace([4,3,5,7,8,2,1]).must_equal(
                [1, 2, 3, 4, 5, 7, 8])


