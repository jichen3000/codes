class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

class safesub(dict):        
    def __missing__(self, key):
        return '{' + key + '}'  


if __name__ == '__main__':
    from minitest import *

    with test("format"):
        s = '{name} has {n} messages.'
        s.format(name='Guido', n=37).must_equal('Guido has 37 messages.')

        name = 'Guido'
        n = 37
        # format_map for python3
        # s.format_map(vars()).must_equal('Guido has 37 messages.')
        s.format(**vars()).must_equal('Guido has 37 messages.')

        # vars().pp()      

        a = Info('Guido',37)
        vars(a).must_equal({'n': 37, 'name': 'Guido'})
        s.format(**vars(a)).must_equal('Guido has 37 messages.')


        # del a.n
        # vars(a).must_equal({ 'name': 'Guido'})
        # s.format(**vars(a)).must_equal('Guido has 37 messages.')

        # del n
        # s.format(**safesub(vars())).must_equal('Guido has 37 messages.')
        pass