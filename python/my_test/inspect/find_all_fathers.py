import inspect
print inspect.getmro(int)


def mm():
    print "mm"
print inspect.getmro(type(mm))
# notice, you cannot run the below one directly
# print inspect.getmro(function)