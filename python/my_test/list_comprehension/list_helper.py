
def is_any_member_in_list(source_list, target_list):
    is_in_list = tuple((label in target_list) for label in source_list)
    return any(is_in_list)

if __name__ == '__main__':
    from minitest import *

    with test('is_any_member_in_list'):
        is_any_member_in_list([1,5], []).must_equal(False)
        is_any_member_in_list([1,5],[2,3,4]).must_equal(False)
        is_any_member_in_list([1,4],[2,3,4]).must_equal(True)
