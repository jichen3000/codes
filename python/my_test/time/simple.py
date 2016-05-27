import time
import datetime 

def _str_to_datetime(the_string, the_format="%Y-%m-%d %H:%M:%S"):
    '''
        Transfer the string like "2014-09-16 14:30:35" to datetime object.
    '''
    struct_time = time.strptime(the_string, the_format)
    return datetime.datetime.fromtimestamp(time.mktime(struct_time))


if __name__ == '__main__':
    from minitest import *

    with test(time.strptime):
        struct_time = time.strptime("2014-09-16 14:30:35", "%Y-%m-%d %H:%M:%S")
        time.strftime("%Y-%m-%d %H:%M:%S", struct_time).must_equal("2014-09-16 14:30:35")
        time.strftime("%Y%m%d_%H%M%S", struct_time).must_equal("20140916_143035")
        # real_time = time.mktime(struct_time)
        # real_time.strftime("%Y-%m-%d %H:%M:%S").p()

    with test(datetime):
        struct_time = time.strptime("2014-09-16 14:30:35", "%Y-%m-%d %H:%M:%S")
        datetime.datetime.fromtimestamp(time.mktime(struct_time)).must_equal(
            datetime.datetime(2014, 9, 16, 14, 30, 35))

    with test(_str_to_datetime):
        _str_to_datetime("2014-09-16 14:30:35").must_equal(
            datetime.datetime(2014, 9, 16, 14, 30, 35))
        _str_to_datetime("2014/09/16 14:30:35", "%Y/%m/%d %H:%M:%S").must_equal(
            datetime.datetime(2014, 9, 16, 14, 30, 35))        