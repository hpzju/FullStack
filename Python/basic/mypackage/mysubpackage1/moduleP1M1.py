print("enter moduleP1M1")

__all__ = ["p1m1", "p1m1_helper", "p2m1"]

from mypackage.mysubpackage2.moduleP2M1 import p2m1


def p1m1():
    print(f"{p1m1.__name__} at {__file__} called")
    print(f"{p1m1.__name__} calling {p2m1.__name__}")
    p2m1()


def p1m1_helper():
    print(f"{p1m1_helper.__name__} at {__file__} called")


if __name__ == '__main__':
    p1m1()


print("exit moduleP1M1")