import turtle


def polygon(n, len, pen, origin=(0, 0),):
    pen.setpos(*origin)
    angle = 360/n
    for i in range(n):
        pen.forward(len)
        pen.left(angle)


if __name__ == "__main__":
    bob = turtle.Turtle()
    polygon(10, 100, bob)

    turtle.mainloop()
