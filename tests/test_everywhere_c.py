'''
Project's testing code
'''

import pytest
from everywhere._base import fib, hello, add42


@pytest.mark.parametrize("test_input, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
])
def test_fib(test_input, expected):
    '''
    test fib
    '''
    assert fib(test_input) == expected


def test_hello():
    '''
    test hello
    '''
    assert hello() == "Hello World"


@pytest.mark.parametrize("test_input, expected", [
    (0, 42),
    (1, 43),
    (-1, 41),
    (-2, 40),
])
def test_add42(test_input, expected):
    '''
    test add42
    '''
    assert add42(test_input) == expected
