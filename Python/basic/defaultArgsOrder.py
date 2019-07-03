def falseOrderFunc(a, b, c, d="default-d", *args, **kwargs):
    print(a, b, c, d, args, kwargs)


def rightOrderFunc(a, b, c, *args, d="default-d",  **kwargs):
    print(a, b, c, args, d, kwargs)


if __name__ == "__main__":
    falseOrderFunc(1, 2, 3, 4, 5, 6, 7, kwa1="kwa1", kwa2="kwa2")

    rightOrderFunc(1, 2, 3, 4, 5, 6, 7, kwa1="kwa1", kwa2="kwa2")

    rightOrderFunc(1, 2, 3, 4, 5, 6, 7, d="changed", kwa1="kwa1", kwa2="kwa2")
