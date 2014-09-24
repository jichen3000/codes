def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def test_answer2():
    assert func(4) == 5

class TestClass:
    def setup_method(self, method):
        self.mm = 'mm'

    def test_one(self):
        x = "this"
        assert 'h' in x
        assert 'mm'==self.mm

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


if __name__ == '__main__':
    import pytest
    pytest.main()