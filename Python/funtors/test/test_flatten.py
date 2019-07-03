from .. import functors


def test_flatten():
    assert functors.flatten([1, 2, 3]) == [1, 2, 3]
