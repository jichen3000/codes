
def median_two_n(a, b):
    return float(a+b)/2
def median_list(the_list, the_len):
    middle_index = the_len / 2
    if the_len % 2 == 0:
        return (median_two_n(the_list[middle_index-1],the_list[middle_index]), middle_index - 0.5)
    else:
        return(the_list[middle_index], middle_index)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print(nums1)
        print(nums2)

        # a is always smaller one
        if len(nums1) > len(nums2):
            nums_a, nums_b = nums2, nums1
        else:
            nums_b, nums_a = nums2, nums1
        len_a, len_b = len(nums_a), len(nums_b)
        if len_a == 0:
            return median_list(nums_b, len_b)[0]
        if nums_a[-1] <= nums_b[0]: 
            return median_list(nums_a+nums_b, len_a+len_b)[0]
        elif nums_a[0] >= nums_b[-1]: 
            return median_list(nums_b+nums_a, len_a+len_b)[0]
        if len_a == 1:
            median_a = nums_a[0]
            if len_b == 1:
                return median_two_n(median_a,nums_b[0])
            elif len_b % 2 == 1:
                median_index = len_b / 2
                if median_a < nums_b[median_index-1]:
                    return median_two_n(nums_b[median_index-1], nums_b[median_index])
                elif nums_b[median_index-1] <= median_a  and median_a <= nums_b[median_index]:
                    return median_two_n(median_a, nums_b[median_index])
                elif nums_b[median_index] < median_a  and median_a <= nums_b[median_index+1]:
                    return median_two_n(median_a, nums_b[median_index])
                elif nums_b[median_index+1] < median_a:
                    return median_two_n(nums_b[median_index], nums_b[median_index+1])
                else:
                    raise Exception("Error: logic error")
            elif len_b % 2 == 0:
                median_big_index = len_b / 2
                median_small_index = len_b / 2 -1
                if median_a <= nums_b[median_small_index]:
                    return nums_b[median_small_index]
                elif median_a >= nums_b[median_big_index]:
                    return nums_b[median_big_index]
                elif median_a > nums_b[median_small_index] and median_a < nums_b[median_big_index]:
                    return median_a
                else:
                    raise Exception("Error: logic error")
        elif len_a == 2:
            # the key part 1
            if len_b == 2:
                return median_two_n(max(nums_a[0],nums_b[0]), min(nums_a[1],nums_b[1]))
            # the key part 2
            elif len_b % 2 == 1:
                new_list = [max(nums_a[0], nums_b[len_b/2-1]), nums_b[len_b/2], 
                            min(nums_a[1], nums_b[len_b/2+1])]
                print("new_list",new_list)
                print(sorted(new_list))

                return sorted(new_list)[1]
            # the key part 3
            elif len_b % 2 == 0:
                new_list = [nums_b[len_b/2] , nums_b[len_b/2-1], 
                        max(nums_a[0], nums_b[len_b/2-2]),
                        min(nums_a[1], nums_b[len_b/2+1])]
                sorted_list = sorted(new_list)
                return median_two_n(sorted_list[1],sorted_list[2])
            else:
                raise Exception("Error: logic error")
        else:
            median_a_index = (len_a-1)/2
            median_b_index = (len_b-1)/2
            if nums_a[median_a_index] <= nums_b[median_b_index]:
                new_nums_a = nums_a[median_a_index:]
                new_nums_b = nums_b[0:len_b-(len_a-len(new_nums_a))]
                return self.findMedianSortedArrays(new_nums_a, new_nums_b)
            else:
                # 3,4, 3.5
                new_nums_a = nums_a[0:len_a/2+1]
                new_nums_b = nums_b[median_a_index:len_b-(len_a-len(new_nums_a))+median_a_index]
                return self.findMedianSortedArrays(new_nums_a, new_nums_b)




# http://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        nums1, nums2 = [1,2,3],[4,5]
        Solution().findMedianSortedArrays(nums1, nums2).must_equal(3)
        nums1, nums2 = [1,2],[4,5]
        Solution().findMedianSortedArrays(nums1, nums2).must_equal(3)




