import re


NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' 
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'


def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield (m.lastgroup, m.group())

if __name__ == '__main__':
    from minitest import *

    with test("token"):
        text = 'foo = 23 + 42 * 10'
        master_pat = re.compile('|'.join(
                [NAME, NUM, PLUS, TIMES, EQ, WS]))

        tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
                      ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
        [t for t in generate_tokens(master_pat, 
                text) if t[0]!='WS'].must_equal(
                tokens)
        pass