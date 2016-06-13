#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""basic functions."""


def fib(number: int) -> int:
    """
    Simple Fibonacci function.

    >>> fib(10)
    55
    """
    if number < 2:
        return number
    else:
        return fib(number-1) + fib(number-2)


def hello() -> str:
    """
    Simple Hello World.

    >>> hello()
    'Hello World'
    """
    return 'Hello World'


def add42(number: int) -> int:
    """
    Add 42 to number.

    >>> add42(100)
    142
    """
    return number + 42
