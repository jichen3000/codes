from functools import partial

print int('100',base=2)
base_two = partial(int, base=2)
print base_two('100')

def test_print(msg1, msg2):
    print "msg: ", msg1, " 2: ",msg2

class A():
    def aa():
        print "aa"

test_print_one = partial(test_print, 'the one')
test_print_one('the two')

def get_local_funcation(local_env, func_name):
    return local_env[func_name]

def is_just_one_argument(func):
    # for int, str something like these methods which are either 'type' or 'function'
    if (type(func).__name__ == 'type'):
        return True
    def for_function():
        return func.func_code.co_argcount == 1
    def for_partial():
        return func.func.func_code.co_argcount-len(func.args) == 1
    return get_local_funcation(locals(), 'for_'+type(func).__name__)()

print dir(is_just_one_argument)
# print str.func_code
print is_just_one_argument(str)
print is_just_one_argument(test_print)
print is_just_one_argument(test_print_one)
# print is_just_one_argument.func_code.co_consts


# print test_print.aa('111')
# # print type(test_print_one)
# print test_print_one.func.func_code.co_argcount