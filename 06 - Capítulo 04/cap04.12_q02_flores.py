# Escreva um conjunto de funções adequadamente geral que possa desenhar flores.

import turtle
import math

mf = turtle.Turtle()
mf.shape("turtle")

def plinha(mf, n, length, angle):
       for i in range(n):
        mf.fd(length)
        mf.lt(angle)


def poligono(mf, n, length):
    angle = 360.0/n
    plinha(mf, n, length, angle)


def plinha(mf, n, length, angle):
       for i in range(n):
        mf.fd(length)
        mf.lt(angle)


def arc(mf, r, angle):
    arc_length = 2 * math.pi * r * (angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    mf.lt(step_angle/2)
    plinha(mf, n, step_length, step_angle)
    mf.rt(step_angle/2)



def petala(mf, r, angle):
    for i in range(2):
        arc(mf, r, angle)
        mf.lt(180-angle)


def flower(mf, n, r, angle):
    for i in range(n):
        petala(mf, r, angle)
        mf.lt(360.0/n)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
    t.speed(50)


move(mf, -100)
flower(mf, 7, 60.0, 60.0)

move(mf, 100)
flower(mf, 10, 40.0, 80.0)

move(mf, 100)
flower(mf, 20, 140.0, 20.0)

mf.hideturtle()
turtle.mainloop()