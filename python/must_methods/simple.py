
if __name__ == '__main__':
    import nose
    from must_methods import gself
    import os
    def setup():
        gself.ls = "ls"
    def test_must_equal():
        print "ok"
        print gself.ls
        'sdd',(1).must_equal(1)

    # support print in the test methods
    os.environ['NOSE_NOCAPTURE'] = '1'
    result = nose.runmodule()

