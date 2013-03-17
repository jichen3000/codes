import sys

print sys.platform
# win32, linux2

import os
print os.name
# nt, posix

import platform
print platform.platform()
# Windows-7-6.1.7601-SP1, 
# Linux-2.6.18-164.el5PAE-i686-with-redhat-5.4-Tikanga

print platform.uname()
# ('Windows', 'chenji-WS', '7', '6.1.7601', 'AMD64', 'Intel64 Family 6 Model 30 Stepping 5, GenuineIntel')
# ('Linux', 'cshdev2', '2.6.18-164.el5PAE', '#1 SMP Tue Aug 18 15:59:11 EDT 2009', 'i686', 'i686')



# do not 
def __linux2_my_path(sub_dir):
    return "/root/"+sub_dir

def __win32_my_path(sub_dir):
    return "C:\\colin\\"+sub_dir

def __linux2_pre_import():
    print "linx2 import"
def __win32_pre_import():
    print "win32 import"

def get_corresponding_function(function_name):
    return eval("__"+sys.platform+"_"+function_name)


# my_path = get_corresponding_function("my_path")
def my_path(sub_dir):
    fun = get_corresponding_function("my_path")
    return fun(sub_dir)

# pre_import = get_corresponding_function("pre_import")
def pre_import():
    fun = get_corresponding_function("pre_import")
    return fun()
pre_import()


print os.path.join(my_path("dd"),"conf")
def main():
    print my_path("dd")

if __name__ == '__main__':
    main()

