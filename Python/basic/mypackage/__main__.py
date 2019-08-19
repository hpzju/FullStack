import mypackage


def info(pkage):
    props = ['__name__', '__package__', '__path__', '__file__',
             '__spec__', '__loader__', '__all__']
    for prop in props:
        print(f"{prop}: {getattr(pkage,f'{prop}')}")


if __name__ == '__main__':
    info(mypackage)
    mypackage.p1m1()
