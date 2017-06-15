from turtle import *

f1 = [[0.15,0.1,-0.4,0.45,0.1],[0.3,-0.1,-0.8,0.5,0.1],[0.15,0.1,-0.8,0.4,0.1],[0.4,0.5,-0.8,0.4,0.3],[0,-0.5,-0.6,-0.5,0]]
donut = [[0,-0.2,-0.1,-0.2,0],[-0.2,0.8,1,0.8,-0.2],[-0.1,1,-3,1,-0.1],[-0.1,0.8,1,0.8,-0.1],[0,-0.1,-0.2,-0.1,0]]
block = [[0.04,0.2,0.2,0.2,0.04],[0.2,1,1,1,0.2],[0.2,1,1,1,0.2],[0.2,1,1,1,0.2],[0.04,0.2,0.2,0.2,0.04]]
getcolor = [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def rand(side=15):
    from random import random
    a = []
    for x in range(side):
        b = []
        for y in range(side):
            b.append(random())
        a.append(b)
    return a

def grid(iterable,numbers=True):
    reset()
    delay(0)
    speed(0)
    hideturtle()
    penup()
    goto(-300,-300)
    seth(45)
    j = 0
    for y in iterable:
        i = 0
        for x in y:
            pendown()
            color(x,x,x)
            begin_fill()
            circle(30,steps=4)
            end_fill()
            if numbers == True:
                if x < 0.5:
                    color(1,1,1)
                else:
                    color(0,0,0)
                penup()
                goto(xcor()-35,ycor()+15)
                write(str(j)+', '+str(i))
                i += 1
                goto(xcor()+35,ycor()-15)
            goto(xcor()+45,ycor())
        j += 1
        penup()
        goto(-300,ycor()+45)

metric = donut # Set what to detect for
sample = rand()
def detect():
    clear()
    intensities = []
    for row in range(15):
        for thing in range(15):
            home = sample[row][thing]
            likeness = 0
            for metrow in range(-2,3):
                for value in range(-2,3):
                    if 0 <= row-metrow < 15 and 0 <= thing-value < 15:
                        process_bit = sample[row-metrow][thing-value]
                    else:
                        process_bit = 0
                    likeness += process_bit*metric[metrow+2][value+2]
            intensities.append(likeness)
    # put intensities on cells
    delay(0)
    speed(0)
    hideturtle()
    penup()
    goto(-300,-300)
    seth(45)
    cell = 0
    for y in sample:
        for x in y:
            pendown()
            color(x,x,x)
            begin_fill()
            circle(30,steps=4)
            end_fill()
            if x < 0.5:
                color(1,1,1)
            else:
                color(0,0,0)
            penup()
            setx(xcor()-30)
            write(str(round(intensities[cell],2)))
            setx(xcor()+75)
            cell += 1
        goto(-300,ycor()+45)
    print('Maximum: '+str(max(intensities)))
    print('Row: '+str(int(intensities.index(max(intensities))/15)))
    print('Column: '+str(intensities.index(max(intensities))%15))
    print('Minimum: '+str(min(intensities)))
    print('Row: '+str(int(intensities.index(min(intensities))/15)))
    print('Column: '+str(intensities.index(min(intensities))%15))
grid(sample)
# Use sample[row][column] = value to change the color of a cell
