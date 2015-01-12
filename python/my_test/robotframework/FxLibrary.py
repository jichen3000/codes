from fx import fx

class FxLibrary:
    def __init__(self):
        self._result = ''

    def return_self(self, the_value):
        self._result = fx(the_value)

    def result_must_be(self, expected_value):
        if self._result != expected_value:
            raise AssertionError("{0} != {1} ".format(self._result, expected_value))