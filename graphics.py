from turtle import *
import time
delay(0)
speed(0)
hideturtle()
title('Trangraphics')

def rectangle(startx,starty,ht,wd): # Starting coordinates are based on the top-left corner
    penup()
    goto(startx,starty)
    pendown()
    forward(wd)
    left(90)
    forward(0-ht)
    left(90)
    forward(wd)
    left(90)
    forward(0-ht)
    left(90)

def line(startX, startY, endX, endY): # Color dependent on pen color
    penup()
    goto(startX, startY)
    pendown()
    goto(endX, endY)

def penHue(hue, mode='pen'): # Sets pen color to specified hue (0-359)
    red = 0
    green = 0
    blue = 0
    retVal = '#'
    if hue <= 60 or hue > 300:
        red = 255
    elif hue > 240 and hue <= 300:
        red = (255/60) * (hue - 240)
    elif hue <= 120 and hue > 60:
        red = 255 - (255/60) * (hue - 60)
    else:
        red = 0
    if hue <= 180 and hue > 60:
        green = 255
    elif hue <= 60:
        green = (255/60) * hue
    elif hue > 180 and hue <= 240:
        green = 255 - ((255/60) * (hue - 180))
    else:
        green = 0
    if hue <= 300 and hue > 180:
        blue = 255
    elif hue <= 180 and hue > 120:
        blue = (255/60) * (hue - 120)
    elif hue > 300:
        blue = 255 - ((255/60) * (hue - 300))
    else:
        blue = 0
    red = hex(round(red))
    if len(red) == 3:
        retVal = retVal + '0'
    retVal = retVal + red[2]
    if len(red) == 4:
        retVal = retVal + red[3]
    green = hex(round(green))
    if len(green) == 3:
        retVal = retVal + '0'
    retVal = retVal + green[2]
    if len(green) == 4:
        retVal = retVal + green[3]
    blue = hex(round(blue))
    if len(blue) == 3:
        retVal = retVal + '0'    
    retVal = retVal + blue[2]
    if len(blue) == 4:
        retVal = retVal + blue[3]
    if mode[0] == 'p':
        pencolor(retVal)
    else:
        fillcolor(retVal)
    return(retVal)

def xgotoclick(button=1):
    onscreenclick(goto, button)
    return xcor()

def ygotoclick(button=1):
    onscreenclick(goto, button)
    return ycor()

def gotoclick(button=1):
    onscreenclick(goto, button)
    return pos

def sprite(name):
    if name in Turtles():
        raise 'NameTakenError: Name already taken'
    name = Turtle()

def move(sprite,distance):
    sprite.fd(distance)

def turn(sprite,distance):
    sprite.right(distance)
