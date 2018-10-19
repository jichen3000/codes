'''
    show how to use generator, every generator is iteration, but not vice verse.
'''
def yrange(n):
    # print n
    i = 0
    # print i
    while i < n:
        # print i
        yield i
        i = i +  1

y_iter = yrange(10)
# print y_iter.next()
# print y_iter.next()
for i in y_iter:
    print i

# if __name__ == "__main__":
#     from minitest import *

#     only_test(yrange)
#     with test(yrange):
#         y_iter = yrange(3)
#         print y_iter.next()
#         print y_iter.next()
