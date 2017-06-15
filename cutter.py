from turtle import *
import time
from statistics import *

delay(0)
speed(0)
hideturtle()
listen()
# Made a change!
def rectangle(startx,starty,ht,wdt): #Starting coordinates are based on the top-left corner
    penup()
    goto(startx,starty)
    pendown()
    forward(wdt)
    left(90)
    forward(0-ht)
    left(90)
    forward(wdt)
    left(90)
    forward(0-ht)
    left(90)

def makecut():
    global last
    pencolor('white')
    pendown()
    width(5)
    if xcor() <= 195:
        sety(120)
        sety(-96)
    cuts.append(xcor()-last)
    last = xcor()
    penup()

reset()
while True:
    cuts = []
    last = -100

    fillcolor('blue')
    begin_fill()
    rectangle(-100,64,128,200)
    end_fill()

    penup()
    seth(90)
    fillcolor('black')
    shape('triangle')
    goto(-100,-96)
    showturtle()
    onkey(makecut,'space')

    for a in range(200):
        setx(a-100)
        time.sleep(0.01)
    makecut()

    reset()
    penup()
    goto(-60,120)
    pencolor('black')
    penup()
    
    write(str(round(pstdev(cuts))),font=('Arial',80,'bold'))
    goto(0,0)
