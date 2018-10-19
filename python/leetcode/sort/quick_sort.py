def quick_sort_inplace(arr):
    """
    :type arr: List[int]
    :rtype: None
    replace in place

    time: O(n log n), space: O(1)
    """
    def helper(l, r):
        if l >= r: return
        i, j = l, r-1
        v = arr[r]
        while i <= j:
            if arr[i] <= v:
                i += 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
        arr[i], arr[r] = arr[r], arr[i]
        helper(l, i-1)
        helper(i+1, r)

    helper(0, len(arr)-1)
    return arr

if __name__ == '__main__':
    from minitest import *

    with test(quick_sort_inplace):
        quick_sort_inplace([4,3,7,8,2,1, 5]).must_equal(
                [1, 2, 3, 4, 5, 7, 8])
        quick_sort_inplace([3,5,1,2,4,8]).must_equal(
                [1, 2, 3, 4, 5, 8])


