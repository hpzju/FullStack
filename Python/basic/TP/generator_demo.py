import sys


def simple_gen(n):
    for i in range(n):
        yield i


def circle_gen(n):
    while True:
        for i in range(n):
            yield i


def inf_gen():
    i = 0
    while True:
        i += 1
        yield i


def echo_gen():
    msg = yield "Priming"
    while True:
        log(f"echo_gen sending: {msg}")
        msg = (yield msg)
        log(f"echo_gen receiving: {msg}")


counter = inf_gen()


def log(*args):
    print(next(counter), ': ', *args)


if __name__ == "__main__":
    # for i in simple_gen(10):
    #     print(i)
    # gen = simple_gen(4)
    # print(f"{iter(gen)} : {gen}")

    gen2 = echo_gen()
    log(next(gen2))

    messageQ = [f'echo {i}' for i in simple_gen(10)]

    for msg in messageQ:
        log(f"in for-loop: {msg}")
        info = gen2.send(msg)
        log(f"info: {info}")
