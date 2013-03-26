import os
import re
from datetime import datetime

__MAJOR = 1
__MINOR = 1
__BUILD = 2
__BUILT_TIME_STR = "2013-03-25 13:59:24"
__BUILT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
__BUILD_NAME = "__BUILD"
__BUILT_TIME_STR_NAME = "__BUILT_TIME_STR"
__BUILT_TIME = datetime.strptime(__BUILT_TIME_STR, __BUILT_TIME_FORMAT)
__BUILD_PATTERN = re.compile('^('+__BUILD_NAME+')\s*=\s*(\d+)')
__BUILT_TIME_PATTERN = re.compile('^('+__BUILT_TIME_STR_NAME+')\s*=\s*"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})"')
__PATTERN_ARRAY = (__BUILD_PATTERN, __BUILT_TIME_PATTERN)

def __read_lines(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()

def __write_lines(file_name, lines):
    with open(file_name, 'w') as f:
        f.writelines(lines)
    return True

def __get_need_change(line):
    for pattern in __PATTERN_ARRAY:
        if pattern.match(line) != None:
            return pattern.match(line)
    return None

def __change_values(line):
    name, value = __get_need_change(line).groups()
    function_name_suffix = name.lower().replace('__','_')
    # fun = eval("__change" + function_name_suffix)
    fun = globals()["__change" + function_name_suffix]
    return fun(line, value)

def __change_built_time_str(line, value):
    return line.replace(value,datetime.now().strftime(__BUILT_TIME_FORMAT))
    

def __change_build(line, value):
    pre_build_no = int(value)
    return line.replace(str(pre_build_no),str(pre_build_no+1))

def __get_info_values():
    match_list = [__get_need_change(line) for line in __read_lines(os.path.realpath(__file__))]
    match_list = filter (lambda a: a != None, match_list)
    match_list = {i.groups()[0]:i.groups()[1] for i in match_list}
    return  match_list

def get_major():
    return __MAJOR

def get_minor():
    return __MINOR

def get_build():
    return __BUILD

def get_built_time():
    return __BUILT_TIME

def __get_version_by_build_str(build_str):
    return str(get_major())+"."+str(get_minor())+"."+build_str

def get_version():
    return __get_version_by_build_str(str(get_build()))

def get_info():
    info_values = __get_info_values()
    return "The current version is "+__get_version_by_build_str(
        info_values[__BUILD_NAME])+", and built time is "+info_values[__BUILT_TIME_STR_NAME]+"."
    
def new_version():
    self_file_name = os.path.realpath(__file__)
    lines = __read_lines(self_file_name)
    new_lines = [__change_values(line) if __get_need_change(line) != None else line for line in lines]
    __write_lines(self_file_name, new_lines)
    return True

if __name__ == '__main__':
    import sys
    if (len(sys.argv) == 2) and (sys.argv[1]=="new_version"):
        new_version()
        print "A new version has been generated!"
        print get_info()
    elif (len(sys.argv) == 2) and (sys.argv[1]=="get_info"):
        print get_info()
    else:
        print "Please use the below commands to generate a new version."
        print "  python gen_version.py new_version"
        print "  python gen_version.py get_info"