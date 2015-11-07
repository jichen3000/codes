import textwrap
import os

s = "Look into my eyes, look into my eyes, the eyes, the eyes, "+\
    "the eyes, not around the eyes, don't look around the eyes, "+\
    " look into my eyes, you're under."

if __name__ == '__main__':
    from minitest import *

    with test(textwrap):
        print textwrap.fill(s, 70)
        print textwrap.fill(s, 40, subsequent_indent='    ')

        # os.get_terminal_size().columns.pp()
        pass