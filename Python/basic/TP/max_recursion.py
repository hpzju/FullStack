import sys


def max_recursion():
    count = 1

    def recursion():
        nonlocal count
        count += 1
        sys.setrecursionlimit(sys.getrecursionlimit() + 1)
        if count == 2000:
            return
        recursion()
    try:
        recursion()
    except Exception as e:
        print(f"Error is: {e}")
    finally:
        print(f"Max Recursion: {count}")


def recurse(n):
    print(n)
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
    recurse(n + 1)


if __name__ == "__main__":
    recurse(1)
    # max_recursion()
    # print(f"system max recursion:{sys.getrecursionlimit()}")
    # max_recursion()
    # print(f"system max recursion after reset:{sys.getrecursionlimit()}")
