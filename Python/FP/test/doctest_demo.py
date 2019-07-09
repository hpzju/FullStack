import sys
import doctest


def doctest_demo(a, b):
    """
    >>> doctest_demo(3, 2)
    5

    >>> doctest_demo(3, 4)
    7

    >>> doctest_demo("str1", "str2")
    'str1str2'

    >>> doctest_demo(3, "3")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


if __name__ == "__main__":
    """
    import doctest module
    run 'python doctest_demo.py -v'
    """
    print(80*"*")
    print(f"run test with: {sys.executable}")
    print(doctest_demo(1, 8))
    print(80*"*")
    print("run doctest_demo:")
    doctest.testmod()
