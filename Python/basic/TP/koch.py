import turtle


def koch(tur, order, len):
    if order == 0:
        tur.forward(len)
    else:
        koch(tur, order-1, len/3)
        tur.left(60)
        koch(tur, order-1, len/3)
        tur.right(120)
        koch(tur, order-1, len/3)
        tur.left(60)
        koch(tur, order-1, len/3)


if __name__ == "__main__":
    window = turtle.Screen()
    t = turtle.Turtle()
    koch(t, 4, 400)
    window.mainloop()
