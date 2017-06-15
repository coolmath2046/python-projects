from turtle import *
from math import *
from random import *
delay(-999999)
speed(0)
colorind = 50
def terra(x,y):
    return randint(-18,18)+(x**2+y**2)-4
def oval(x,y):
    global colorind
    colorind = 200
    return x**2+((y**2)*2)
def square(x,y):
    global colorind
    colorind = 220
    return ((x**12)+(y**12))/5012296
def heart(x,y):
    global colorind
    colorind = 280
    return (x**2+((1.25*y)-abs(x))**2)+4.8
def disk(x,y):
    return (x**2+y**2)-4
def sun(x,y):
    return -1*(x**2+y**2)-4
def ufo(x,y):
    return (x**3+y**3)
def sine(x,y):
    return (10*(sin(x)+sin(y)))
def diamond(x,y):
    global colorind
    colorind = 174
    return abs(x)*4+abs(y)*4
def flower(x,y):
    global colorind
    colorind = 300
    petals = 5
    return 25*cos(petals*(atan2(y,x)))+(x**2+y**2)-5
def penhue(h, mode='pen'): #Sets pen color to specified hue (0-359)
    red = 0
    green = 0
    blue = 0
    hue = h % 360
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
    if len(retVal)==7:
        return(retVal)
    else:
        return('#B6B6B6')
minx = -10
maxx = 10
miny = -10
maxy = 10
hideturtle()
penup()
goto(45 * minx, 45 * miny)
pendown()
for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        seth(45) # otherwise, the square would look like a diamond.
        if abs(flower(x,y)) > 35.97:
            color('#FFFFFF', '#000000')
        else:
            penhue(colorind+flower(x,y)*1.5)
            penhue(colorind+flower(x,y)*1.5, mode='fill')
        begin_fill()
        circle(45*0.71+2, steps=4) # makes a square
        end_fill()
        seth(0)
        if x < 10:
            forward(45)
    penup()
    backward(2*maxx*45)
    seth(90)
    forward(45)
    pendown()
    seth(0)
        
    
