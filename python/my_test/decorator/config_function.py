func_dict = {}
def config(the_func):
    func_name = the_func.func_name
    func_dict[func_name] = the_func
    return the_func

@config
def user_rule(msg):
    print "user_rule: " + msg

@config
def name_rule(msg):
    print "name_rule: " + msg   


if __name__ == '__main__':
    from minitest import *

    with test('funcs'):
        func_dict.pp()
        name_rule('123')
        

