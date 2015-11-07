# a grammar for simple arithmetic expressions
# BNF
#     expr ::= expr + term
#          |   expr - term
#          | term
    
#     term ::= term * factor
#          |   term / factor
#          | factor
    
#     factor ::= ( expr )
#            |   NUM

# EBNF
#     expr ::= term { (+|-) term }*
#     term ::= factor { (*|/) factor }*
#     factor ::= ( expr )
#            |   NUM

# packages: PLY, PyParsing