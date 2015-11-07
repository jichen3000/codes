# ved_lad@symantec.com
    
def get_all_str_recursively(the_str):
    result = []
    if len(the_str) <= 1:
        return [the_str]
    if len(the_str) == 2:
        return [the_str, the_str[::-1]]
    for i in range(len(the_str)):
        the_list = get_all_str_recursively(remove_one(the_str, i))
        for l in the_list:
            result.append(the_str[i] +l)
    return result

def get_all_str_o(the_str):
    count = len(the_str)
    if count <= 1:
        return the_str
    if count == 2:
        return [the_str, the_str[::-1]]
    last_two = the_str[-2:]
    cur_list = [last_two, last_two[::-1]]
    for i in range(count-3,-1,-1):
        cur_list = [insert_one(cur_str, the_str[i] , j) for cur_str in cur_list for j in range(len(cur_str)+1)]
    return cur_list

def insert_one(the_str, insert_one, i):
    # (the_str, insert_one, i).p()
    return the_str[0:i]+insert_one+the_str[i:]

def remove_one(the_str, i):
    if len(the_str) <= 2:
        return the_str[1-i]
    if i == 0:
        return the_str[1:]
    if i == len(the_str) - 1:
        return the_str[:-1]
    return the_str[0:i] + the_str[i+1:]



if __name__ == '__main__':
    from minitest import *
    with test(get_all_str_recursively):
        get_all_str_recursively('abcd').size().must_equal(24)
        get_all_str_recursively('abcd').pp()

    with test(get_all_str_o):
        get_all_str_o('abc').size().must_equal(6)
        get_all_str_o('abcd').size().must_equal(24)
        # get_all_str_o('abcd').must_equal(get_all_str_recursively('abcd'))

    with test(insert_one):
        insert_one('abc','d',0).must_equal('dabc')
        insert_one('abc','d',1).must_equal('adbc')
        insert_one('abc','d',3).must_equal('abcd')
        insert_one('abc','d',6).must_equal('abcd')
