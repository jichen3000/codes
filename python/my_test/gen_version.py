import ConfigParser
import os.path as path
import time

VERSION_FILE_NAME = path.join(path.dirname(path.realpath(__file__)),"version.dat")
MAJOR_VERSION = 1
MINOR_VERSION = 2
VERSION_SECTION_NAME = "version"
CURRENT_VERION_ITEM_NAME = "current"



def __new_version():
    # example: 1.2.20130313144942
    # rule: MAJOR_VERSION+MINOR_VERSION+time_str
    return str(MAJOR_VERSION)+"."+str(
        MINOR_VERSION)+"."+time.strftime("%Y%m%d%H%M%S",time.localtime())

def __write_version_file():
    config = ConfigParser.RawConfigParser()
    config.add_section(VERSION_SECTION_NAME)
    config.set(VERSION_SECTION_NAME, CURRENT_VERION_ITEM_NAME,__new_version())
    with open(VERSION_FILE_NAME, 'wb') as config_file:
        config.write(config_file)
    return True

def get_version():
    config = ConfigParser.RawConfigParser()
    config.read(VERSION_FILE_NAME)
    return config.get(VERSION_SECTION_NAME,CURRENT_VERION_ITEM_NAME)

def __test():
    __write_version_file()
    print get_version()
    print "ok"

if __name__ == '__main__':
    import sys
    if (len(sys.argv) == 2) and (sys.argv[1]=="new_version"):
        __write_version_file()
        print "The new version( "+get_version()+" ) has been generated!"
    elif (len(sys.argv) == 2) and (sys.argv[1]=="test"):
        __test()
    else:
        print "Please use the below command to generate a new version."
        print "  python gen_version.py new_version"
