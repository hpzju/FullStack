def my_func_consts():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 10
    f = [1, 2] * 5


def my_func_membership():
    if e in [1, 2, 3]:
        pass


if __name__ == '__main__':

    print(my_func_consts.__code__.co_consts)

    print(my_func_membership.__code__.co_consts)