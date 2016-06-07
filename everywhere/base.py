#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(number: int) -> int:
    if number < 2:
        return number
    else:
        return fib(number-1) + fib(number-2)


def hello() -> None:
    return "Hello World"


def add42(number: int) -> int:
    return number + 42
