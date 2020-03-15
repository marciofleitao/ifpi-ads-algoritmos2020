# Desenhe um diagrama da pilha que mostre o estado do programa enquanto executa circle (bob, radius).

import turtle
import math
def square(mf, r):
    mf = turtle.Turtle()
    mf.shape("turtle")
    r = 100
    mf.pu()
    mf.fd(r)
    mf.lt(90)
    mf.pd()
    circle(mf, r)
    mf.speed(50)

    turtle.mainloop()


def circle(mf, r):
    arc(mf, r, 360)


def arc(mf, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    mf.lt(step_angle/2)
    plinha(mf, n, step_length, step_angle)
    mf.rt(step_angle/2)



def plinha(mf, n, length, angle):
       for i in range(n):
        mf.fd(length)
        mf.lt(angle)


def poligono(mf, n, length):
    angle = 360.0/n
    plinha(mf, n, length, angle)


square('',1050)
