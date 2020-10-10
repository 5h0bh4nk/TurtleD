from turtle import *
from random import random
from freegames import line

def drawmaze():
    color('red')
    width(5)

    for i in range(-200,200,40):
        for j in range(-200,200,40):
            if random() > 0.5:
                line(i,j,i+40,j+40)
            else:
                line(i,j+40,i+40,j)
    update()

def tap(x,y):
    "drawing line and dot for screen tap"
    if abs(x)>198 or abs(y)>198:
        up()
    else:
        down()
    
    width(2)
    color('blue')
    goto(x,y)
    dot(4)

setup(420,429,370,0)
hideturtle()
tracer(False)
drawmaze()
onscreenclick(tap)
done()
