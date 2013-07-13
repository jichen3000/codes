import time, sys
def my_sleep(i):
    time.sleep(1)
    print str(i)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print "start " + sys.argv[1]
    else:
        print "start"
    [ my_sleep(i) for i in range(5)]
    print "ok"