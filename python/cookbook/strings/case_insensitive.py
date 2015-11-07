import re

if __name__ == '__main__':
    from minitest import *

    text = 'UPPER PYTHON, lower python, Mixed Python' 
    with test("findall"):
        re.findall('python', text, flags=re.IGNORECASE).must_equal(
            ['PYTHON', 'python', 'Python'])

    with test("sub"):
        re.sub('python', 'snake', text, flags=re.IGNORECASE).must_equal(
            'UPPER snake, lower snake, Mixed snake')

        def matchcase(word): 
            def replace(m):
                text = m.group() 
                if text.isupper():
                    return word.upper() 
                elif text.islower():
                    return word.lower() 
                elif text[0].isupper():
                    return word.capitalize() 
                else:
                    return word 
            return replace
        re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE).must_equal(
            'UPPER SNAKE, lower snake, Mixed Snake')
