from turtle import *
import time
side = 16 # start() creates a [side] by [side] grid.
setundobuffer(1)
speed(0)
delay(0)
huge = 40/side
t = []
master = []
penup()
load = Turtle(visible=False)
load.penup()
load.goto(-100,400)
def loaded(pct):
    load.clear()
    load.write(str(pct)+'% loaded',font=('Arial',24,'normal'))
    
def turtle_create():
    for i in range(side):
        turtlelist = []
        masterlist = []
        for j in range(side):
            turtlelist.append(Turtle(shape='square'))
            masterlist.append('black')
            turtlelist[j].penup()
            turtlelist[j].speed(0)
            turtlelist[j].shapesize(huge)
        t.append(turtlelist)
        master.append(masterlist)
        loaded(round((i+1)/side*75,2))

def grid():
    for row in range(side):
        for square in range(side):
            t[row][square].goto(row*huge*20-side*huge*10,square*huge*20-side*huge*10)
        if row%3 == 2:
            loaded(round((row+1)/side*25+75,2))

# Syntax for specifying square: t[x][y]

def gridcoords(x,y):
    return (round((x+400)/(20*huge)),round((y+400)/(20*huge)))

def cartesiancoords(x,y):
    return (x*20*huge-side*10*huge,y*20*huge-side*10*huge)

def state(to_color,x,y):
    t[x][y].fillcolor(to_color)
    master[x][y] = to_color

def life():
    import life
