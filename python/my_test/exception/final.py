
def test_final():
    try:
        1/0
        return "ok"
    # except Exception, e:
    #     raise e
    finally:
        print 'in finally'
        

if __name__ == '__main__':
    from minitest import *

    with test(test_final):
        test_final().pp()
