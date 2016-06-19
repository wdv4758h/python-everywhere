"""basic functions in Cython."""


cpdef int fib(int number):
    """
    Simple Fibonacci function.

    >>> fib(10)
    55
    """
    if number < 2:
        return number
    return fib(number-1) + fib(number-2)


cpdef str hello():
    """
    Simple Hello World.

    >>> hello()
    'Hello World'
    """
    return 'Hello World'


cpdef int add42(int number):
    """
    Add 42 to number.

    >>> add42(100)
    142
    """
    return number + 42
