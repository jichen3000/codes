import types

def must_equal(target, x):
    print "x=",x
    print "called from", target 

Person.must_equal = types.MethodType(must_equal, Person)
colin.must_equal("mm")

# However, you cannot use this meaming to add a method to object.
# object.must_equal1 = types.MethodType(must_equal, object)
# colin.must_equal1("mm")
