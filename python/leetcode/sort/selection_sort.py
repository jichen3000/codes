def selection_sort(arr):
    """
    :type arr: List[int]
    :rtype: None
    replace in place

    time: O(n**2), space: O(1)
    """    
    n = len(arr)
    if n <= 1: return
    for i, v in enumerate(arr):
        min_v, min_i = v, i
        for j in range(i+1, n):
            if arr[j] < min_v:
                min_v, min_i = arr[j], j
        if min_i != i:
            arr[i], arr[min_i] = arr[min_i], arr[i]
    return


if __name__ == '__main__':
    from minitest import *

    with test(selection_sort):
        arr = [6,5,7,8,4,3]
        selection_sort(arr)
        arr.must_equal([3, 4, 5, 6, 7, 8])
