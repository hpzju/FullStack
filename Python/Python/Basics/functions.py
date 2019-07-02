

def adder(lhv):
    def inner(rhv):
        return lhv + rhv
    return inner


if __name__ == "__main__":
    print("hello.")
    a5 = adder(5)
    a = adder(4)(4)
    b = a5(100)
    print(a5, a, b)
