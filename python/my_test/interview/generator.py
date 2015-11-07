''' 
    show how to use generator, every generator is iteration, but not vice verse.
'''
def yrange(n):
    i = 0
    if i < n:
        print i
        yield i
        i += 1

y_iter = yrange(3)
print y_iter.next()
print y_iter.next()
# if __name__ == "__main__":
#     from minitest import *

#     only_test(yrange)
#     with test(yrange):
#         y_iter = yrange(3)
#         print y_iter.next()
#         print y_iter.next()