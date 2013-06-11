import argparse
import sys

import method_route

EXECUTABLE_METHOD_NAMES = ['simple1','simple2','simple3', 'module1', 'module2', 'module3']
MODULE_NAMES = ['atom','atomdaemon']

def gen_parse():
    parser = argparse.ArgumentParser( 
        description="show how to invoke methods by arguments")
    parser.add_argument('methods', help='execute method names: '+','.join(EXECUTABLE_METHOD_NAMES))
    parser.add_argument('--modules', default=','.join(MODULE_NAMES), help='module names: '+','.join(MODULE_NAMES))
    return parser

def simple1():
    print "simple1"
def simple2():
    print "simple2"
def simple3():
    print "simple3"

def module1(module_name):
    print "module1",module_name
def module2(module_name):
    print "module2",module_name
def module3(module_name):
    print "module3",module_name

def __get_func_info(func):
    # argments count and names
    return [module1.func_code.co_argcount, module1.func_code.co_varnames]


def main(args):
    module_list = args.modules.split(',')
    [method_route.call_method_with_special_arg(
        method_route.get_funcation_in_env(globals(), method_name),
        module_list,
        'module_name') 
        for method_name in args.methods.split(',')]

if __name__ == '__main__':
    print method_route.get_funcation_in_env(globals(),'module1')
    print "sys.argv",sys.argv,len(sys.argv)
    if len(sys.argv)==1:
        sys.argv.append(','.join(EXECUTABLE_METHOD_NAMES))
    parser = gen_parse()
    args = parser.parse_args()
    print "args:",args
    print "methods", args.methods
    print "modules", args.modules
    main(args)