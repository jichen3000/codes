# pip install mock
from mock import MagicMock
from mock import patch

def my_func(x):
    return x

if __name__ == '__main__':
    from minitest import *

    with test(MagicMock):
        m = MagicMock(return_value = 10)
        m(1, 2, debug=True).must_equal(10)
        m(1, 2).must_equal(10)
        m(4,5).must_equal(10)

    with test(patch):
        # patch can be used as decorator
        with patch('__main__.my_func') as mock_func:
            my_func(1)
            mock_func.assert_called_with(1)


