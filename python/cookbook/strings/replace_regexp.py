import re

if __name__ == '__main__':
    from minitest import *

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.' 
    with test("re sub"):
        re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text).must_equal(
                'Today is 2012-11-27. PyCon starts 2013-3-13.')

    with test("month"):
        from calendar import month_abbr
        def change_date(m):
            mon_name = month_abbr[int(m.group(1))]
            return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

        datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
        datepat.sub(change_date, text).must_equal(
                'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.')

        # get how many substiutions.
        datepat.subn(r'\3-\1-\2', text).must_equal(
                ('Today is 2012-11-27. PyCon starts 2013-3-13.', 2))

