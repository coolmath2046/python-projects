from turtle import *
from random import randint

number = 0
getting_number = False

def initialize():
    title('Math Dice')
    bgcolor('#894104')
    roll()
    goto(-430,316)
    color('white','white')
    write('Player 1, press A to write your answer.',font=('Monospace',26,'normal'))
    goto(-191,267)
    write('Player 2, use L.',font=('Monospace',26,'normal'))
def roll(dummyx=0,dummyy=0):
    random = [randint(1,12),randint(1,12),randint(1,6),randint(1,6),randint(1,6)]
    target = random[0]*random[1]
    scoring = [random[2],random[3],random[4]]
    penup()
    shape('square')
    delay(0)
    speed(0)
    goto(-100,0)
    hideturtle()
    shapesize(1.3)
    for x in range(2,5):
        color('blue','blue')
        stamp()
        color('white','white')
        goto(xcor()-4,ycor()-17)
        write(str(random[x]),font=('Arial',18,'bold'))
        goto(xcor()+104,ycor()+17)
    goto(-65,100)
    for x in range(2):
        color('white','white')
        pendown()
        begin_fill()
        circle(30,steps=5)
        end_fill()
        color('black','black')
        penup()
        goto(xcor()+1,ycor()+6)
        write(str(random[x]),align='center',font=('Arial',27,'bold'))
        goto(xcor()+129,ycor()-6)
initialize()
def key1():
    global number
    number = number*10+1
def key2():
    global number
    number = number*10+2
def key3():
    global number
    number = number*10+3
def key4():
    global number
    number = number*10+4
def key5():
    global number
    number = number*10+5
def key6():
    global number
    number = number*10+6
    
def getNumber():
    global number,getting_number
    getting_number = True
    while getting_number == True:
        bind()
def unbind():
    
while True:
    onscreenclick(roll)
    onkeypress(getNumber,a)
    onkeypress(getNumber,l)
    done()
    
