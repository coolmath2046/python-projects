from turtle import *
from random import *
from timeit import *
import math
import time

# list of games: Greenlight, Tower, Names, Meteor

array = [] # general array for any games
score = 0 # general score counter for any games
score2 = 0 # general dual score counter for any games
life = 1 # general life counter for any games
ok = 1 # general turtle overlap troubleshooter for any games

delay(0)
speed(0)
shape('circle')
shapesize(0.5,0.5,0)
listen()

def reset_game(): # not a game
    time.sleep(1.5)
    clear()
    global array
    global score
    global life
    global ok
    global score2
    array = []
    score = 0
    life = 1
    score2 = 0
    ok = 1 

def points(x,y,prevscore,add): # not a game
    coords = (xcor(),ycor())
    penup()
    goto(232,-240)
    pencolor('white')
    write('Score: ' + str(prevscore), font=('Helevetica',16,'normal'))
    global score
    global score2
    score += add
    score2 += 1
    time.sleep(0.1)
    pencolor('black')
    write('Score: ' + str(score), font=('Helevetica',16,'normal'))
    penup()
    goto(coords)


def Greenlight(): # press the green squares. Avoid the red ones.
    title('Green Light')
    seth(45)
    width(25)
    penup()
    def init():
        goto(-270,360)
        write('Press the green squares. Avoid the red ones.', font=('Helevetica',22,'normal'))

    def look(a,b):
        global score
        global ok
        global life
        ok = 0
        life = 0
        prevscore = score
        if array[round((9*round((b+220)/50))+(a+200)/50-18.5)] == 'g' and life != round((9*round((b+220)/50))+(a+200)/50-18.5):
            width(25)
            life = round((9*round((b+220)/50))+(a+200)/50-18.5)
        elif life == round((9*round((b+220)/50))+(a+200)/50-18.5):
            score = -2146473648
        elif score > 6 and score > -1:
            score -= 6
        else:
            score = 0
        points(0,-240,prevscore,1)
        ok = 1

    def grid(mode=0):
        goto(-150,-150)
        for x in range(9):
            for y in range(9):
                pendown()
                while ok == 0:
                    fd(0) # do nothing
                if randint(1,4) == 3:
                    fillcolor('green')
                    if mode == 0:
                        array.append('g')
                    else:
                        array[9*x+y] = 'g'
                else:
                    fillcolor('red')
                    if mode == 0:
                        array.append('r')
                    else:
                        array[9*x+y] = 'r'
                begin_fill()
                circle(radius=35.4,steps=4) # draws a square
                end_fill()
                penup()
                setx(xcor()+50) # moves the turtle to the absolute right 50 pixels
            setx(-150)
            sety(ycor()+50)
    init()
    grid()
    onscreenclick(look)
    t = time.process_time()
    while time.process_time() < 5+t:
        grid(mode=1)
    goto(300,0)
    write('Time up!', font=('Helevetica',32,'normal'))
    reset_game()
    Greenlight()   

def Tower(): # Press space to jump. Avoid the red.
    title('Impossible Tower')
    penup()
    goto(-200,-1000)
    pendown()
    sety(1000)
    setx(200)
    sety(-1000)
    penup()
    goto(-200,-400)
    for x in range(32):
        s = randint(0,352)
        array.append(s) # gap is 48 pixels across
    def world():
        for x in range(32):
            seth(0)
            pencolor('red')
            f = array[x]
            pendown()
            fd(f)
            penup()
            fd(48)
            pendown()
            fd(352-f)
            penup()
            setx(-200)
            sety(ycor()+48)
    world()
    penup()
    goto(-180,-378)
    def look():
        global score
        prevscore = score
        if abs((array[score2+1]-176)-xcor()) < 16:
            sety(ycor()+48)
            points(232,-240,prevscore,1)
        else:
            penup()
            goto(-250,0)
            pendown()
            pencolor('black')
            write('You died!', font=('Helevetica',72,'normal'))
            reset_game()
            Tower()
        penup()
    onkeypress(look,'space')
    while True:
        while xcor() < 177:
            seth(0)
            fd(1+(score2/5))
        while xcor() > -177:
            seth(180)
            fd(1+(score2/5))

def Names(times=100,myseed=random()+7*11,gilli=12345):
    bye()
    seeda = myseed ** 1.01
    def seeds(seednum,maximum):
        seed(seednum)
        return int(round(random()*maximum-0.5))

    def one(seeda):
        # some letters may appear more than once in a row to make them more likely to get picked.
        vowels = ['a','a','e','e','i','i','o','u','y']
        vb = ['ai','ea','ee','ie','oa','oi','oo','ou']
        con0 = ['l','r']
        con1 = ['b','b','c','c','ch','f','f','g','g','p','p','s','s','s','sc','sh','sk','st','sp','t','t','t']
        con2 = ['bb','cc','d','d','dd','ff','gg','h','h','h','j','k','l','l','l','ll','ll','m','m','m','mm','n','n','n','nn','pp','qu','r','r','r','rr','sm','sn','ss','th','th','tt','v','w','w','x','y','z','zz']
        a = seeds(seeda,2)+2
        result = ''
        for b in range(a):
            d = seeds(seeda,5)
            if d <= 2:
                result = result + con1[seeds(seeda+b,len(con1))]
            elif d == 3:
                result = result + con1[seeds(seeda+0.125+b,len(con1))] + con0[seeds(seeda+0.25,2)]
            else:
                result = result + con2[seeds(seeda+0.375+b,len(con2))]
            if b != a-1 or randint(1,2) == 2:
                if randint(1,5) == 1:
                    result = result + vb[seeds(seeda+0.5+b,len(vb))]
                else:
                    result = result + vowels[seeds(seeda+0.75+b,len(vowels))]
        if gilli == 1:
            result = result + 'y'
        print(result)
    for e in range(times):
        one(seeda+e)
pressed = 0        
def Meteor(): # D to go right, A to go left. Avoid the meteors. Best played on fullscreen.
    title('Meteor')
    start = time.clock()
    turtle = Turtle()
    turtle2 = Turtle()
    turtle3 = Turtle()
    turtle4 = Turtle()
    turtle5 = Turtle()
    turtle6 = Turtle()
    turtle7 = Turtle()
    turtle8 = Turtle()
    turtle9 = Turtle()
    turtle10 = Turtle()
    turtle11 = Turtle()
    turtle12 = Turtle()
    array = [turtle,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8,turtle9,turtle10,turtle11,turtle12]
    for thing in array:
        thing.shape('circle')
        thing.color('white','#884400')
        thing.shapesize(5)
        thing.penup()
        thing.direction = randint(210,330)
        thing.speed = 3*random()
        thing.goto(randint(-600,600),randint(-48,353))
    turtle.color('white','#6969FF')
    def stars():
        hideturtle()
        bgcolor('#000000')
        for x in range(59):
            pendown()
            dot(randint(2,10),'white')
            penup()
            goto(randint(-930,930),randint(-500,500))
        showturtle()
    stars()
    array.remove(turtle)
    turtle.penup()
    turtle.goto(0,-343)
    def right():
        global pressed
        pressed = 1
        while pressed != 0:
            turtle.fd(10)
            meteors(5+2*(time.clock()-start))
    def left():
        global pressed
        pressed = 1
        while pressed != 0:
            turtle.bk(10)
            meteors(5+2*(time.clock()-start))
    def stop():
        global pressed
        pressed = 0
    onkeypress(right,'d')
    onkeypress(left,'a')
    onkeyrelease(stop,'d')
    onkeyrelease(stop,'a')
    def distance(p1,p2):
        return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
    def meteors(gp):
        player_pos = turtle.pos()
        for thing in array:
            thing.seth(thing.direction)
            thing.fd(gp+thing.speed)
            if thing.ycor() < -450:
                thing.hideturtle()
                thing.goto(randint(-500,500),450)
                thing.direction = randint(int(210+(-0.1*thing.xcor())),int(330-(-0.1*thing.xcor())))
                thing.showturtle()
            if distance(thing.pos(),player_pos) < 75:
                global life
                life = 0
                pencolor('white')
                goto(-250,0)
                write('You died!', font=('Helevetica',72,'normal'))
                goto(-63,-52)
                write('Score: ' + str(int(((gp-5)/2)**2*96)), font=('Helevetica',18,'normal'))
                time.sleep(2)
                life = 1
                for thing in array:
                    thing.hideturtle()
                    thing.goto(0,1000)
                turtle.goto(0,1000)
                clear()
                Meteor()
    while True:
        meteors(5+2*(time.clock()-start))
        if life == 0:
            break

def Highway():
    title('Highway')
    window = Screen()
    window.screensize()
    window.setup(width = 1.0, height = 1.0)
    car_pos = []
    turtles = []
    cars = 10
    lanes = [-200,-100,0,100,200]
    def road():
        for x in range(-250,300,100):
            penup()
            goto(x,-500)
            pendown()
            goto(x,550)
        penup()
        goto(0,-250)
    def setup():
        colors = ['red','yellow','green','blue']
        for x in range(cars):
            turtles.append(Turtle(shape='square'))
        for x in turtles:
            x.penup()
            x.color(colors[randint(0,3)])
            x.shapesize(stretch_wid=5,stretch_len=2)
            x.showturtle()
            x.speed = cars
            while True:
                ok = 1
                x.goto(lanes[randint(0,4)],randint(-600,1000))
                position = x.pos()
                for y in car_pos:
                    if (position[0] == y[0] and abs(position[1]-y[1]) < 140) or (abs(position[0]) < 6 and -370 < position[1] < 470):
                        ok = 0
                if ok == 1:
                    car_pos.append(position)
                    break
    def collision(cars, focus_car, speed, turtles):
        q = 0
        x = turtles[focus_car]
        for y in cars:
            if abs(x.pos()[0] - y[0]) < 40 and 0 < y[1]-x.pos()[1] < 140:
                x.sety(x.ycor()-(speed*0.8))
                turtles[q].sety(turtles[q].ycor()+(speed*0.6))
            if abs(x.pos()[0] - pos()[0]) < 1 and -350 < x.pos()[1] < -150:
                hideturtle()
                goto(-250,0)
                write('You died!', font=('Helevetica',72,'normal'))
                print(time.clock()-1)
                for thing in turtles:
                    thing.hideturtle()
                    thing.setx(350)
                turtles = []
                time.sleep(2)
                showturtle()
                clear()
                Highway()
            q += 1
    road()
    setup()
    penup()
    shape('square')
    shapesize(stretch_wid=5,stretch_len=2)
    def right():
        speed(0.3)
        fd(100)
        speed(0)
    def left():
        speed(0.3)
        bk(100)
        speed(0)
    onkeypress(right,'d')
    onkeypress(left,'a')
    while True:
        n = 0
        for x in turtles:
            x.sety(x.ycor()-x.speed)
            car_pos[n] = x.pos()
            if x.ycor() < -600:
                x.hideturtle()
                x.goto(lanes[randint(0,4)],randint(600,1000))
                x.showturtle()
            collision(car_pos,n,x.speed,turtles)
            n += 1
            x.sety(x.ycor()-x.speed)        
Names()
