if __name__ == '__main__':
    from minitest import *
    import re
    line = "asdf fd; kk, mm,    ff"

    with test("without delimiters"):
        re.split(r'[;,\s]\s*', line).must_equal(
                ['asdf', 'fd', 'kk', 'mm', 'ff'])

    with test("with delimiters"):
        fields = re.split(r'(;|,|\s)\s*', line)
        fields.must_equal(
                ['asdf', ' ', 'fd', ';', 'kk', ',', 'mm', ',', 'ff'])

        fields[::2].must_equal(['asdf', 'fd', 'kk', 'mm', 'ff'])
        fields[1::2].must_equal([' ', ';', ',', ','])

    with test("using parentheses without delimiters"):
        re.split(r'[;,\s]\s*', line).must_equal(
                ['asdf', 'fd', 'kk', 'mm', 'ff'])
