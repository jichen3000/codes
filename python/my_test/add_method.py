import types

class A(object):#but seems to work for old style objects too
    pass

def patch_me(target):
    def method(target,x):
        print "x=",x
        print "called from", target
    target.method = types.MethodType(method,target)
    #add more if needed

a = A()
print a
#out: <__main__.A object at 0x2b73ac88bfd0>  
patch_me(a)    #patch instance
a.method(5)
#out: x= 5
#out: called from <__main__.A object at 0x2b73ac88bfd0>
patch_me(A)
A.method(6)        #can patch class too
#out: x= 6
#out: called from <class '__main__.A'>

b = A()
b.method(10)


def method2(target,x):
    print "x=",x
    print "called from", target
A.method2 = types.MethodType(method2,A)

b.method2(99)


# can't set attributes of built-in/extension type 'dict'
def delete_for_dict(target, key):
    del target[key]
    return target

dict.delete = types.MethodType(delete_for_dict,dict)

aa = {None:123, 333:444}

print aa
aa.delete(None)
print aa