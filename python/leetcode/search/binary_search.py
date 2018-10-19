def binary_search(nums, target):
    """
    input: int[] nums, int target
    return: int
    """
    if not nums: return -1
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# search the fist one which less than target in nums
def binary_search_upbound_index(nums, target):
    n = len(nums)
    low, high = 0, n-1
    while low < high:
        mid = (low+high) // 2
        if nums[mid] < target:
            low = mid+1
        # elif nums[mid] == target:
        #     return mid
        else:
            high = mid
    return low

if __name__ == '__main__':
    from minitest import *

    with test(binary_search):
        nums = [1,3,5,7,9,11]
        binary_search(nums, 8).must_equal(-1)
        binary_search(nums, 7).must_equal(3)
        binary_search(nums, 2).must_equal(-1)
        
    with test(binary_search_upbound_index):
        nums = [1,3,5,7,9,11]
        binary_search_upbound_index(nums, 8).must_equal(4)
        binary_search_upbound_index(nums, 7).must_equal(3)
        binary_search_upbound_index(nums, 2).must_equal(1)


