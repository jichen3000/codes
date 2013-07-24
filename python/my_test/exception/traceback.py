import sys
import traceback

# def run_user_code():
#     source = "ls -l"
#     try:
#         exec source in {}
#     except:
#         print "Exception in user code:"
#         print '-'*60
#         traceback.print_exc(file=sys.stdout)
#         print '-'*60

# envdir = {}
# while 1:
#     run_user_code(envdir)
# run_user_code()
# traceback.format_exc()
# print sys.version_info
# print "ok"


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print e
    import traceback
    print traceback.format_exc()
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise