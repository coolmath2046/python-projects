from grid import *
from turtle import *
from random import *

turtle_create()
grid()
title("War of Conway")
message = 'Tap a living cell to kill it,\n or a dead cell to birth it.'

sacrifice = 0
killed = 0
birth = False
processing = False
players = 0

load.penup()
load.clear()
load.write('Game of Life',font=('Arial',24,'normal'))

player1 = 'Vincent'
player2 = 'Daddy'
color1 = 'red'
color2 = 'blue'

turn = Turtle(visible=False)
turn.player = color2
turn.penup()
turn.clicks = []
bgcolor('#CCCCCC')
penup()
ht()
speed(0)
delay(0)
print('''Controls: Left click to birth/kill, space to do a Life iteration,
right-click to write all the neighbor counts (zero player), r to randomly fill, c to clear,
and g for a game of GOLAD.''')

def change(x,y):
    global sacrifice, killed, birth, players
    x1 = gridcoords(x,y)[0]
    y1 = gridcoords(x,y)[1]
    if players == 0:
        statemap = {'white':'black','black':'white'}
    elif turn.player == color1:
        statemap = {'black':color1,color1:'black',color2:'black'}
    else:
        statemap = {'black':color2,color1:'black',color2:'black'}
    if x1 < 0 or y1 < 0:
        pass
    else:
        try:
            current = master[x1][y1]
            to_color = statemap[current]
            if players == 0:
                state(to_color,x1,y1)
            else:
                if killed == 1:
                    return
                if to_color == 'black' and killed == 0:
                    if sacrifice == 0:
                        message = 'Tap space to finish your move.'
                        killed = 1
                    elif current == turn.player:
                        sacrifice -= 1
                    else:
                        return
                elif sacrifice == 0:
                    message = 'Tap two living cells to sacrifice\n for the new birth.'
                    sacrifice = 2
                    birth = True
                state(to_color,x1,y1)
                print_neighbors(x1,y1)
                turn.clicks.append((x1,y1))
        except IndexError:
            pass

def neighbors(x,y):
    n = 0
    def removeifin(value):
        if value in check:
            check.remove(value)
    check = [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1)]
    if y == 0:
        removeifin((1,-1))
        removeifin((0,-1))
        removeifin((-1,-1))
    if y == side-1:
        removeifin((1,1))
        removeifin((-1,1))
        removeifin((0,1))
    if x == 0:
        removeifin((-1,1))
        removeifin((-1,0))
        removeifin((-1,-1))
    if x == side-1:
        removeifin((1,-1))
        removeifin((1,1))
        removeifin((1,0))
    for i in check:
        if master[i[0]+x][i[1]+y] != 'black':
            n += 1
    return n

def two_neighbors(x,y):
    red = 0
    Green = 0
    def removeifin(value):
        if value in check:
            check.remove(value)
    check = [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1)]
    if y == 0:
        removeifin((1,-1))
        removeifin((0,-1))
        removeifin((-1,-1))
    if y == side-1:
        removeifin((1,1))
        removeifin((-1,1))
        removeifin((0,1))
    if x == 0:
        removeifin((-1,1))
        removeifin((-1,0))
        removeifin((-1,-1))
    if x == side-1:
        removeifin((1,-1))
        removeifin((1,1))
        removeifin((1,0))
    for i in check:
        if master[i[0]+x][i[1]+y] == color1:
            red += 1
        if master[i[0]+x][i[1]+y] == color2:
            Green += 1
    if red>Green:
        return color1
    else:
        return color2
def lifeiter():
    global processing, players, sacrifice, killed, message, birth
    if processing == False and sacrifice == 0 and killed <= 1:
        clear()
        processing = True
        turn_white = []
        turn_black = []
        turn_red = []
        turn_Green = []
        for x in range(side):
            for y in range(side):
                item = master[x][y]
                neigh = neighbors(x,y)
                if item == 'black':
                    if players == 0:
                        if neigh == 3:
                            turn_white.append((x,y))
                    elif neigh == 3:
                        col = two_neighbors(x,y)
                        if col == color1:
                            turn_red.append((x,y))
                        else:
                            turn_Green.append((x,y))
                else:
                    if neigh not in [2,3]:
                        turn_black.append((x,y))
        for i in turn_black:
            state('black',i[0],i[1])
        for i in turn_white:
            state('white',i[0],i[1])
        for i in turn_red:
            state(color1,i[0],i[1])
        for i in turn_Green:
            state(color2,i[0],i[1])
        if players == 2:
            turn.color('#333333')
            turn.write(message,font=('Arial',20,'normal'))
            message = 'Tap a living cell to kill it,\n or a dead cell to birth it.'
            switch()
            sacrifice = 0
            killed = 0
            birth = False
            print_all_neighbors()
        processing = False

def print_neighbors(x1,y1):
    for x in range(x1-1,x1+2):
        for y in range(y1-1,y1+2):
            if x < 0 or y < 0:
                pass
            else:
                try:
                    cartX = cartesiancoords(x,y)[0]
                    cartY = cartesiancoords(x,y)[1]
                    item = master[x][y]
                    neigh = neighbors(x,y)
                    goto(cartX,cartY)
                    pencolor(item)
                    dot(19*huge)
                    if players == 0:
                        if item == 'black':
                            pencolor('white')
                        else:
                            pencolor('black')
                    else:
                        if item != 'black':
                            pencolor('white')
                            if neigh not in [2,3]:
                                pencolor('black')
                        else:
                            if neigh is not 3:
                                pencolor('#333333')
                            elif two_neighbors(x,y) == color1:
                                pencolor(color1)
                            else:
                                pencolor(color2)
                    goto(cartX-huge*4,cartY-huge*8)
                    write(neigh,font=('Helevetica',int(huge*10),'bold'))
                except IndexError:
                    pass
    updatecells()

def print_all_neighbors(a=0,b=0):
    clear()
    for x in range(side):
        for y in range(side):
            cartX = cartesiancoords(x,y)[0]-huge*4
            cartY = cartesiancoords(x,y)[1]-huge*8
            item = master[x][y]
            neigh = neighbors(x,y)
            goto(cartX,cartY)
            if players == 2:
                if item != 'black':
                    pencolor('white')
                    if neigh not in [2,3]:
                        pencolor('black')
                else:
                    if neigh is not 3:
                        pencolor('#333333')
                    elif two_neighbors(x,y) == color1:
                        pencolor(color1)
                    else:
                        pencolor(color2)
            else:
                if item == 'black':
                    pencolor('white')
                else:
                    pencolor('black')
            write(neigh,font=('Helevetica',int(huge*10),'bold'))
def oppstate(a,b):
    x1 = gridcoords(a,b)[0]
    y1 = gridcoords(a,b)[1]
    if turn.player == color2:
        state(color1,x1,y1)
    else:
        state(color2,x1,y1)
    print_neighbors(x1,y1)

def randfill():
    global players
    players = 0
    clear()
    for x in range(20):
        for y in range(20):
            if randint(1,16) <= 5:
                state('white',x,y)
            else:
                state('black',x,y)

def tworandfill():
    clear_all()
    global players
    players = 2
    onscreenclick(oppstate,btn=3)
    x = randint(0,side-1)
    y = randint(0,side-1)
    for i in range(int(side*side*0.16)):
        while master[x][y] != 'black' or (x == side/2-0.5 and y == side/2-0.5):
            x = randint(0,side-1)
            y = randint(0,side-1)
        state(color1,x,y)
        state(color2,(side-1)-x,(side-1)-y)
    switch()
    print_all_neighbors()

def clear_all():
    for x in range(side):
        for y in range(side):
            state('black',x,y)

def updatecells():
    def count(grid,item):
        return sum(row.count(item) for row in grid)
    turn.goto(600,0)
    turn.color('#CCCCCC')
    turn.dot(430)
    turn.color('black')
    turn.goto(415,90)
    turn.write(message,font=('Arial',20,'normal'))
    turn.color(color1)
    turn.goto(415,0)
    turn.write(player1 + ' has '+str(count(master,color1))+' cells.',font=('Arial',20,'normal'))
    turn.color(color2)
    turn.goto(415,-30)
    turn.write(player2 + ' has '+str(count(master,color2))+' cells.',font=('Arial',20,'normal'))

def switch():
    turn.clear()
    updatecells()
    turn.color('black')
    turn.goto(415,60)
    turn.write('press Space to do a move.',font=('Arial',20,'normal'))
    turn.goto(415,30)
    if turn.player == color1:
        turn.player = color2
        turn.color(color2)
        turn.write(player2+"'s turn.",font=('Arial',20,'normal'))
    else:
        turn.player = color1
        turn.color(color1)
        turn.write(player1+"'s turn.",font=('Arial',20,'normal'))


listen()
onscreenclick(change)
onkeypress(lifeiter,'space')
onkeypress(randfill,'r')
onkeypress(tworandfill,'g')
onkeypress(clear_all,'c')
onscreenclick(print_all_neighbors,btn=3)
done()
