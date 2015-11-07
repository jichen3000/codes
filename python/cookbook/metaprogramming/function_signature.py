from funcsigs import signature, Parameter

if __name__ == '__main__':
    from minitest import *

    with test("signature"):
        parms = [ 
                    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
                    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42), 
                    Parameter('z', Parameter.KEYWORD_ONLY, default=None) 
                ]
        sig = signature(parms)