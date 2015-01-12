import sys

def main(args):
    # args = parser.parse_args()
    args.func(args)
    
def analyze(exclude_arg):
    return '--exclude=user,machine'.split("=")[1].split(",")



if __name__ == '__main__':
    from minitest import *

    sys.argv.p()
    if len(sys.argv)==1:
        sys.argv=sys.argv+['--exclude=user,machine']
    analyze(sys.argv[1]).p()
    print "end!"