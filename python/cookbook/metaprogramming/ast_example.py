import ast

class CodeAnalyzer(ast.NodeVisitor): 
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set() 
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load): 
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store): 
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del): 
            self.deleted.add(node.id)

if __name__ == '__main__':
    from minitest import *

    with test("easy"):
        ex = ast.parse('2 + 3*4 + x', mode='eval')
        ast.dump(ex).must_equal(
                "Expression(body=BinOp(left=BinOp(left=Num(n=2), "+
                "op=Add(), right=BinOp(left=Num(n=3), op=Mult(), "+
                "right=Num(n=4))), op=Add(), right=Name(id='x', "+
                "ctx=Load())))")
        pass
    with test(""):
        top = ast.parse('for i in range(10): print(i); del i', mode='exec')
        c = CodeAnalyzer() 
        c.visit(top) 
        c.loaded.must_equal(set(['i', 'range']))
        c.stored.must_equal(set(['i']))
        c.deleted.must_equal(set(['i',]))
