from macropy.core.macros import *
from pprint import pprint as pp

macros = Macros()

@macros.expr
def expand(tree, **kw):
    print dir(tree)
    print real_repr(tree)
    print unparse(tree)
    return tree
