import os
import re
from datetime import datetime

__MAJOR = 1
__MINOR = 2
__BUILD = 3
__BUILT_TIME_STR = "2013-03-20 16:47:50"
__BUILT_TIME = datetime.strptime(__BUILT_TIME_STR,'%Y-%m-%d %H:%M:%S')
__BUILD_PATTERN = re.compile('^(__BUILD)\s*=\s*(\d+)')
__BUILT_TIME_PATTERN = re.compile(''^(__BUILT_TIME_STR)\s*=\s*"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})"'')

def get_major():
    return __MAJOR

def get_minor():
    return __MINOR

def get_build():
    return __BUILD

def get_built_time():
    return __BUILT_TIME

def __read_lines(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()

def __write_lines(file_name, lines):
    with open(file_name, 'w') as f:
        return f.writelines(lines)

def is_need_change(line):
    return __BUILD_PATTERN.match(line) != None

def change_values(line):
    name, value = __BUILD_PATTERN.match(line).groups()

def change_built_time(line, value):
    now = datetime.now().strftime('%Y%m%d%H%M%S')

def change_version(line, value):
    pre_build_no = int(value)
    return line.replace(str(pre_build_no),str(pre_build_no+1))


def gen_version():
    self_file_name = os.path.realpath(__file__)
    lines = __read_lines(self_file_name)
    new_lines = [change_version(line) if is_need_change(line) else line for line in lines]
    print new_lines
    # __write_lines(self_file_name, lines)

if __name__ == '__main__':
    gen_version()