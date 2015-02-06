from fx import fx
from minitest import *
from robot.libraries.BuiltIn import BuiltIn

class FxLibrary:
    def __init__(self):
        self._result = ''

    def return_self(self, the_value):
        # print "*WARN* This text will show up on the console." + str(BuiltIn().get_variables())
        self._result = fx(the_value)

    def result_must_be(self, expected_value):
        if self._result != expected_value:
            raise AssertionError("{0} != {1} ".format(self._result, expected_value))