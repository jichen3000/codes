
print str.__bases__

import inspect
print inspect.getmro(str)
print inspect.getmro(unicode)

print 'split' in dir(basestring) 
print 'split' in dir(str) 
print 'split' in dir(unicode) 

strs.split("s s", " ")