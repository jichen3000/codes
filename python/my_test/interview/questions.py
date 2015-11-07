# Ramashri Umale: Write a function that takes an array of integers 
# and returns that array rotated by N positions. 
# For example, if N=2, given the input array [1, 2, 3, 4, 5, 6] the function should 
# return [5, 6, 1, 2, 3, 4]

def ratate_list(the_list, rotate_index):
    if rotate_index > len(the_list) and rotate_index < 0:
        raise "Error: rotate_index is out of length of the list"
    start_index = len(the_list) - rotate_index
    return the_list[start_index:] + the_list[:start_index]

print ratate_list([1, 2, 3, 4, 5, 6], 2)

def ratate_list2(the_list, rotate_num):
    for i in range(rotate_num):
        last = the_list[-1]
        for j in range(len(the_list)):
            tmp = the_list[j]
            the_list[j] = last
            last = tmp

    return the_list

print ratate_list2([1, 2, 3, 4, 5, 6], 2)

