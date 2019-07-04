def adder(a, b):
    return a + b


def adder10(a):
    return adder(a, 10)


class Pet(object):
    __counter = 0

    def __init__(self, name):
        Pet.__counter += 1
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
