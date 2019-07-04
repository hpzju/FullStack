import sys
import doctest


def doctestDemo(a, b):
    """
    >>> doctestDemo(3, 2)
    7

    >>> doctestDemo(3, 4)
    7

    >>> doctestDemo("str1", "str2")
    'str1str2'

    >>> doctestDemo(3, "3")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


if __name__ == "__main__":
    """
    import doctest module
    run 'python test_doctestDemo.py -v'
    """
    print(80*"*")
    print(f"run test with: {sys.executable}")
    print(doctestDemo(1, 8))
    print(80*"*")
    print("run docktest:")
    doctest.testmod()
