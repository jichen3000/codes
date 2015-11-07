def has_duplicate_using_set(the_list):
    return len(the_list) - len(set(the_list)) > 0

def has_duplicate_using_in(the_list):
    for index, value in enumerate(the_list):
        if value in the_list[:index]:
            return True
    return False

if __name__ == '__main__':
    from minitest import *

    unique_list = range(4)
    duplicate_list = range(4) + [1]
    with test(has_duplicate_using_set):

        has_duplicate_using_set(duplicate_list).must_true()
        has_duplicate_using_set(unique_list).must_false()

    with test(has_duplicate_using_in):

        has_duplicate_using_in(duplicate_list).must_true()
        has_duplicate_using_in(unique_list).must_false()
        pass