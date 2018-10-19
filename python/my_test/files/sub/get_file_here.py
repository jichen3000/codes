import os

def get_file():
    print("__file__ : ",__file__)
    print(os.path.abspath("."))
    print(os.path.dirname(os.path.abspath(".")))
    print(os.path.abspath(os.path.curdir))