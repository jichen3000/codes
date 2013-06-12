class ColinTest(object):
    allow_reuse = 1
    """docstring for ColinTest"""
    def __init__(self, arg):
        super(ColinTest, self).__init__()
        self.arg = arg
    def pa(self):
        return self.allow_reuse


ct = ColinTest("a")
print dir(ColinTest)
print setattr(ColinTest,'allow_reuse',0)
print ct.pa()
        