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
traceback.format_exc()
print sys.version_info
print "ok"