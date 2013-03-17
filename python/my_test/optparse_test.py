# the module has be Deprecated, please use argparse module
import optparse

def main():
    parser = optparse.OptionParser(usage="usage: %prog module-name "+
        "[-m] [-v] [-q] [-c]", 
        version="%prog 0.1")
    parser.add_option("-m", "--mode", 
        dest="mode", help='Mode')
    parser.add_option("-v", action="store_true", 
        dest="verbose", default=False, help="Verbose")
    parser.add_option("-q", action="store_false", 
        dest="verbose", default=True, help="Quiet [default]")
    parser.add_option("-c", action="store")
    (options, args) = parser.parse_args()
    if len(args)!=1:
        parser.print_help()
        exit()
    else:
        print args[0]

    print "args",args
    print "len args", len(args)
    print "options", options
    print "ok"

def with_module():
    import sys
    print "sys.argv", sys.argv
    module_names = ("answer","validate")
    if len(sys.argv)<2 or (sys.argv[1] not in module_names):
        parser = optparse.OptionParser(usage="usage: %prog "+
            "module-name["+"|".join(module_names)+"] "+
            "[-m] [-v] [-q] [-c]  hello world", 
            version="%prog 0.1")
        parser.print_help()
        exit()
    else:
        apply(eval(sys.argv[1]),[sys.argv])

def answer(sys_argv):
    parser = optparse.OptionParser(usage="usage: %prog answer "+
        "[-m]", 
        version="%prog 0.1")
    parser.add_option("-m", "--multi", 
        dest="multi", help='Multi hello')
    (options, args) = parser.parse_args(sys_argv)
    print "args",args
    print "len args", len(args)
    print "options", options
    print "ok"

def validate(sys_argv):
    parser = optparse.OptionParser(usage="usage: %prog validate "+
        "[-r]", 
        version="%prog 0.1")
    parser.add_option("-r", "--return", 
        dest="return", help='Multi')
    (options, args) = parser.parse_args(sys_argv)
    print "args",args
    print "len args", len(args)
    print "options", options
    print "ok"

def callback_fun():
    print "it is callback_fun!"

if __name__ == '__main__':
    with_module()
