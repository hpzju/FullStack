import decimal
from decimal import Decimal


if __name__ == '__main__':

    x = Decimal('0.25')
    y = Decimal('0.35')
    print(round(x, 1), round(y, 1))
    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_HALF_UP
        print(round(x, 1), round(y, 1))
    print(round(x, 1), round(y, 1))

    print(decimal.getcontext().rounding)

    list(map(lambda x: print(f"Decimal({x}) {decimal.getcontext().rounding}: {round(Decimal(x))}\n"),
        ('1.2', '-1.2', '1.5', '-1.5', '2.5', '-2.5', '3.5', '-3.5', '4.5', '-4.5')))

    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_HALF_UP
        print(ctx.rounding)
        l = list(map(Decimal, ('1.2', '-1.2', '1.5', '-1.5', '2.5', '-2.5', '3.5', '-3.5', '4.5', '-4.5')))
        print(l)
        list(map(lambda x: print(f"{x} {decimal.getcontext().rounding}: {round(x, 0)}\n"),
           l))
