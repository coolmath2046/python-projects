from turtle import *
width(1)
delay(0)
speed(0)
shapesize(3)
shape('circle')
listen()
def glide(x,y):
    penup()
    goto(x,y)
    pendown()
def wipe():
    clear()
    global master
    master = []
    for _ in range(5):
        m = []
        for __ in range(5):
            m.append(1.0)
        master.append(m)
    grid()
def go(x,y): # Lower-left square is (-343,-303)
    goto(x,y)
    squareX = 0
    squareY = 0
    for thing in listX:
        if thing > x:
            break
        squareX += 1
    for thing in listY:
        if thing > y:
            break
        squareY += 1
    global taps
    master[squareX][squareY-1] *= 0.85
def grid():
    color('#a3a3a3','white')
    hideturtle()
    penup()
    goto(-300,-300)
    seth(45)
    for i in range(5):
        for x in range(5):
            begin_fill()
            pendown()
            c = master[x][i]
            fillcolor(c,c,c)
            circle(96,steps=4)
            end_fill()
            penup()
            setx(xcor()+135)
        goto(-300,ycor()+135)
listX = []
listY = []
master = []
for x in range(-343,288,135):
    listX.append(x)
print(len(listX))
for y in range(-303,328,135):
    listY.append(y)
for _ in range(5):
    m = []
    for __ in range(5):
        m.append(1.0)
    master.append(m)
width(5)
grid()
pencolor('#282828')
showturtle()
while True: # Space to clear, enter to value cells
    onclick(go)
    ondrag(go)
    onscreenclick(glide)
    onkeypress(wipe,'space')
    onkeypress(grid,'\r')
    done()
