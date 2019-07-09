print("enter moduleP1M1")

from mypackage.mysubpackage2.moduleP2M1 import p2m1
import sys


print(sys.path)


def p1m1():
    print(f"{p1m1.__name__} at {__file__} called")
    print(f"{p1m1.__name__} calling {p2m1.__name__}")
    p2m1()


if __name__ == '__main__':
    p1m1()


print("exit moduleP1M1")