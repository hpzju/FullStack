from FP.functors import *
import os

print(os.getcwd())


print(dir())
print(__package__)


def test_flatten():
    assert [1, 2, 3] == [1, 2, 3]
