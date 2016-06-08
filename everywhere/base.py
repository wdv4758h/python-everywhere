#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(number: int) -> int:
    '''
    >>> fib(10)
    55
    '''
    if number < 2:
        return number
    else:
        return fib(number-1) + fib(number-2)


def hello() -> str:
    '''
    >>> hello()
    'Hello World'
    '''
    return 'Hello World'


def add42(number: int) -> int:
    '''
    >>> add42(100)
    142
    '''
    return number + 42
