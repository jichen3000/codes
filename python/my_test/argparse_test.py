import argparse
import sys
def answer(args):
    print "answer me!!",args
    print args.x
def gen_parse():
    parser = argparse.ArgumentParser(prog="test", description="main")
    subparsers = parser.add_subparsers()
    answer_parser = subparsers.add_parser("answer", 
        description="this is fro answer module", help="h answer")
    answer_parser.set_defaults(func=answer)
    answer_parser.add_argument('-x', 
        help="a mysterious function")
    return parser

def main(args):
    # args = parser.parse_args()
    args.func(args)
    


if __name__ == '__main__':
    print "sys.argv",sys.argv
    if len(sys.argv)==1:
        sys.argv=sys.argv+['answer', '-x', 'xxx']
    parser = gen_parse()
    args = parser.parse_args()
    main(args)
    print "end!"