import re

if __name__ == '__main__':
    from minitest import *

    str_pat = re.compile(r'\"(.*)\"')
    with test("shortest"):
        text1 = 'Computer says "no."'
        str_pat.findall(text1).must_equal(
                ['no.'])
        text2 = 'Computer says "no." Phone says "yes."' 
        str_pat.findall(text2).must_equal(
                ['no." Phone says "yes.'])

        # add ?
        str_pat = re.compile(r'\"(.*?)\"')
        str_pat.findall(text2).must_equal(
                ['no.', 'yes.'])

        str_pat = re.compile(r'\((.*?)\)')
        text3 = ' ((1 + 2) * 3 + 1) * (1+3)' 
        str_pat.findall(text3).must_equal(
                ['no.', 'yes.'])
