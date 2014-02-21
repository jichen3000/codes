
def ff(count, other):
    print count
    return False, count+1, other

def continue_call_until_no_change(called_func, max_no_changed_count, *args):
    ''' it asks the called_func should return the values which are its own arguments except the first one,
    and the first one is a bool which means if it is changed.
    '''
    no_changed_count = 0
    print type(args)
    results =(True,) + args
    while(no_changed_count < max_no_changed_count):
        results = called_func(*results[1:])
        if results[0]:
            ''' changed '''
            no_changed_count = 0
        else:
            no_changed_count += 1
    return results[1:]


if __name__ == '__main__':
    from minitest import *

    with test("continue_call_until_no_change"):
        continue_call_until_no_change(ff, 4, 100, 11).pp()
