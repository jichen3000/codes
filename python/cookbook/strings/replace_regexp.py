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

    with test("ip port"):
        the_str1 = 'GET /index.php?text=%3ciframe%20src=javascript:'+\
                'alert(/xss/)%3e%3c/iframe%3e HTTP/1.1\r\n'+\
                'Host: 10.200.3.42:8000\r\nConnection: keep-alive\r\n'+\
                'Accept: text/html,application/xhtml+xml,application/xml;'+\
                'q=0.9,image/webp,*/*;q=0.8\r\nUser-Agent: Mozilla/5.0'
        ip_port_pat = re.compile(r'(Host:\s+[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})(:\d+)?')
        match_result = ip_port_pat.search(the_str1)
        match_result.groups().size().must_equal(2)
        match_result.groups().must_equal(("Host: 10.200.3.42",":8000"))
        new_str1 = ip_port_pat.subn(r'\1'+':9999', the_str1)
        match_result = ip_port_pat.search(new_str1[0])
        match_result.groups().must_equal(("Host: 10.200.3.42",":9999"))

        the_str2 = 'GET /index.php?text=%3ciframe%20src=javascript:'+\
                'Host: 10.200.3.42\r\nConnection: keep-alive\r\n'+\
                'q=0.9,image/webp,*/*;q=0.8\r\nUser-Agent: Mozilla/5.0'
        match_result = ip_port_pat.search(the_str2)
        match_result.groups().size().must_equal(2)
        match_result.groups().must_equal(("Host: 10.200.3.42",None))
        new_str2 = ip_port_pat.subn(r'\1'+':9999', the_str2)
        # new_str2.p()
        match_result = ip_port_pat.search(new_str2[0])
        match_result.groups().must_equal(("Host: 10.200.3.42",":9999"))
