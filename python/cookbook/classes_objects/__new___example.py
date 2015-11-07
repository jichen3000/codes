from time import localtime

class MyDate(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls) 
        t = localtime() 
        d.year = t.tm_year 
        d.month = t.tm_mon 
        d.day = t.tm_mday 
        return d

if __name__ == '__main__':
    from minitest import *

    with test(MyDate):
        d = MyDate.__new__(MyDate)
        # d.year
        (lambda : d.year).must_raise(AttributeError, "'MyDate' object has no attribute 'year'")
        
        today = MyDate.today()
        today.year