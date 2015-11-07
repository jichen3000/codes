import re

if __name__ == '__main__':
    from minitest import *

    with test("multi line"):
        comment = re.compile(r'/\*(.*?)\*/')
        text1 = '/* this is a comment */'
        text2 = '''/* this is a
                 multiline comment */'''
        comment.findall(text1).must_equal([' this is a comment '])
        comment.findall(text2).must_equal([])

        multiline_comment = re.compile(r'/\*((?:.|\n)*?)\*/')
        multiline_comment.findall(text1).must_equal([' this is a comment '])
        multiline_comment.findall(text2).must_equal(
                [' this is a\n                 multiline comment '])

        other_comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
        other_comment.findall(text1).must_equal([' this is a comment '])
        other_comment.findall(text2).must_equal(
                [' this is a\n                 multiline comment '])
        pass