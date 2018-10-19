import fileinput
import sys
import re

def replace_all_in_file(file,search_exp,replace_exp):
    for line in fileinput.input(file, inplace=1):
        if re.search(search_exp,line):
            line = re.sub(search_exp,replace_exp, line)
        sys.stdout.write(line)

if __name__ == '__main__':
    from minitest import *

    with test(replace_all_in_file):
        replace_all_in_file('test.txt', '(?:[0-9]{1,3}\.){3}[0-9]{1,3}\s+ec2-gpu', '1.1.1.1\tec2-gpu')

