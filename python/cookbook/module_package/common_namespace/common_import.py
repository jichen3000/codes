# not work in python2
import sys
sys.path.extend(['foo', 'bar'])
print sys.path
import spam.foo
import spam.bar