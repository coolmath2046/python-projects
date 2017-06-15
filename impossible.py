from turtle import *
from random import *
from timeit import *
import math
import time

# list of games: Tower, Ten


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

################################################################################
#                       START OF IMPOSSIBLE GAMES                              #
################################################################################

def tower():
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
            Games.tower()
        penup()
    onkeypress(look,'space')
    while True:
        while xcor() < 177:
            seth(0)
            fd(1+(score2/5))
        while xcor() > -177:
            seth(180)
            fd(1+(score2/5))
checked = False
def ten():
    title('Impossible 10')
    ht()
    colors = ['red','yellow','green','blue','magenta']
    shapes = ['arrow','turtle','circle','square','triangle','classic']
    sizes = [4,10,24]
    random_number = 0
    def rand_config():
        # There are 5 colors, 6 shapes, and 3 sizes. Refer to lines 113-115.
        colors = ['red','yellow','green','blue','magenta']
        p = colors[randint(0,4)]
        pencolor(p)
        colors.remove(p)
        q = colors[randint(0,3)]
        fillcolor(q)
        r = shapes[randint(0,5)]
        shape(r)
        s = sizes[randint(0,2)]
        shapesize(s,s,s)
        if r == 'arrow':
            return (-2*s,s*5,s*4)
        elif r == 'classic':
            return (s*11,s*5,s*3)
        else:
            return (s*6,s*8,s*6)
    
    def check(a,b):
        global checked
        checked = True
        print(a)
        p = pencolor() # Outline
        q = fillcolor() # Color
        r = shape() # Shape
        s = shapesize()[2] # Size
        t = random_number # Number
        master_list = [p,q,r,s,t]
        master_dict = {'Outline':p,'Color':q,'Shape':r,'Size':s,'Number':t}
        def game_over():
            print("Required attribute: "+str(generic_value))
            print("Object's attribute: "+str(master_dict[c[0]]))
            quit()
        if a is None:
            if master_dict[c[0]] == generic_value:
                print('No click; unequal values expected.')
                game_over()
        else:
            if master_dict[c[0]] != generic_value:
                print('Screen clicked; equal values expected.')
                game_over()
        
    master = [['Outline',colors],['Color',colors],['Shape',shapes],\
              ['Size',sizes],['Number',[1,2,3,4,5,6,7,8,9,10]]]
    c = master[randint(0,len(master)-1)]
    value = c[1][randint(0,len(c[1])-1)]
    generic_value = value
    if value == 'classic':
        value = 'dart'
    if c[0] == 'Size':
        if value == 4:
            value = 'small'
        elif value == 10:
            value = 'medium'
        else:
            value = 'big'
    criteria = c[0] + ' must be ' + str(value)
    print(criteria)
    def main():
        while True:
            global checked
            checked = False
            x = 1
            bgcolor('white')
            clear()
            s = rand_config()
            stamp()
            penup()
            goto(xcor()-s[0]/2,ycor()-s[1]/2)
            pendown()
            store_pen = pencolor()
            pencolor('black')
            global random_number
            random_number = randint(1,10)
            write((str(random_number)),font=('Monospace',s[2],'normal'))
            penup()
            pencolor(store_pen)
            goto(xcor()+s[0]/2,ycor()+s[1]/2)
            onscreenclick(check)
            time.sleep(x+0.2)
            print(checked)
            if not checked:
                check(None,None)
                biggies = 99999
        x *= 0.97
    main()
    
        
        
available = [tower,ten]
# available[0]()
ten()
