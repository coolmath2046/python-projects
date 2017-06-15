from grid import *
from turtle import *
from random import *
title('Conquest')
turtle_create()
ht()
grid()
load.penup()
load.clear()
load.write('Conquest',font=('Arial',24,'normal'))
write1 = Turtle(visible=False)
write2 = Turtle(visible=False)
write1.goto(396,45)
write2.goto(396,15)
color1 = '#FF5000'
color2 = '#FF00FF'
numbers = [[0 for i in range(16)] for i in range(16)]
listen()
if side%2 == 1:
    raise ValueError('Side "'+side+'" must be odd')
            
def clear_all():
    for x in range(side):
        for y in range(side):
            state('black',x,y)
            
def randval():
    clear()
    for x in range(side):
        for y in range(int(side/2)):
            armies = randint(randint(1,2),randint(5,8))
            cartX = cartesiancoords(x,y)[0]-huge*4
            cartY = cartesiancoords(x,y)[1]-huge*8
            for _ in range(2):
                numbers[x][y] = armies
                numbers[side-1-x][side-1-y] = armies

###############################################################################
#                               CREATING REGIONS                              #
###############################################################################
armies = numbers
visited = [[0 for i in range(16)] for j in range(16)]
regionValue = 0
armyData = {}              
def floodfill(surface, x, y, oldColor=None, newColor=0):
    global visited, armyData, regionValue, armies
    rows = len(surface)
    columns = len(surface[0])
    if x > -1 and y > -1:
        try:
            if oldColor is None:
                oldColor = surface[x][y]
            if surface[x][y] != oldColor: # the base case
                return
            surface[x][y] = newColor
            if regionValue in armyData:
                armyData[regionValue] += armies[x][y]
            else:
                armyData[regionValue] = armies[x][y]
            visited[x][y] = newColor
        except IndexError:
            return
        floodfill(surface,x + 1, y, oldColor, newColor) # right
        floodfill(surface,x - 1, y, oldColor, newColor) # left
        floodfill(surface,x, y + 1, oldColor, newColor) # down
        floodfill(surface,x, y - 1, oldColor, newColor) # up

def combine():
    global armyData, regionValue
    s = master
    regionValue = 0
    for x in range(16):
        for y in range(16):
            if s[x][y] in [color1,color2,'green']:
                floodfill(s,x,y,None,str(regionValue))
                regionValue += 1
    for key in armyData:
        key = str(key)
        searchFor = [(index, row.index(key)) for index, row in enumerate(s) if key in row]
        t = cartesiancoords(searchFor[0][0],searchFor[0][1])
        num = armyData[int(key)]
        goto(t[0]-huge*2*(len(str(num))+1),t[1]-huge*8)
        write(num,font=('Arial',int(48/(len(str(num))+1)),'bold'))
                
def tworandfill():
    global armies,visited,regionvalue,armyData
    snum = randint(1,1000000) # Set the seed
    seed(snum)
    write1.clear()
    write1.write('Game PIN: '+str(snum),font=('Arial',20,'bold'))
    clear_all() 
    x = randint(0,side-1)
    y = randint(0,side-1)
    for i in range(int(side*side*0.5)):
        color1 = '#FF5000'
        color2 = '#FF00FF'
        while master[x][y] != 'black' or (x == side/2-0.5 and y == side/2-0.5):
            x = randint(0,side-1)
            y = randint(0,side-1)
        if randint(1,4) == 1:
            color1 = 'green'
            color2 = 'green'
        state(color1,x,y)
        state(color2,(side-1)-x,(side-1)-y)
    randval()
    armies = numbers
    visited = [[0 for i in range(16)] for j in range(16)]
    regionValue = 0
    armyData = {}  
    printArmies()

def printArmies(a=0,b=0):
    clear()
    combine()

def move(x,y):
    try:
        tile = gridcoords(x,y)
        write2.clear()
        write2.write('Region Value:' + master[tile[0]][tile[1]],font=('Arial',20,'bold'))
    except IndexError:
        pass
    
def battle(a,b):
	''' This is how many soldiers are killed. '''
	if a<b:a,b=b,a
	return (a+b)-round((a+b)*(1-(b/a)**2))

onkeypress(tworandfill,'g')
onscreenclick(move)
