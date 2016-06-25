from theano import tensor as T, function, printing
x = T.dvector()
hello_world_op = printing.Print('hello world')
printed_x = hello_world_op(x)
f = function([x], printed_x)
r = f([1, 2, 3])
# hello world __str__ = [ 1.  2.  3.]