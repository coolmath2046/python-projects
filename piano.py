from turtle import *
right = 0
wrong = 0
pendown()
listen()
hideturtle()
pencolor('black')
def plusRight():
    global right
    right += 1
    clear()
    write((str(100*right/(right+wrong)))+'%',font=('Arial',40,'normal'))
def plusWrong():
    global wrong
    wrong += 1
    clear()
    write((str(100*right/(right+wrong)))+'%',font=('Arial',40,'normal'))
def reset():
    global right, wrong
    right = 0
    wrong = 0
    clear()
while True: # r for right, w for wrong, space for reset
    onkeypress(plusRight,'r')
    onkeypress(plusWrong,'w')
    onkeypress(reset,'space')
    done()
    
