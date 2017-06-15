from turtle import *
from random import *

size = 10
cells = []
unit = 400/size
position = size+3
visited = []

def initialize(): # make the black box
    goto(-240,-240)
    begin_fill()
    for i in range(4):
        fd(480)
        lt(90)
    end_fill()
    penup()
    goto(-200+unit/2,-200+unit/2)
    
def create_array(): # create the master array of cells' states
    for i in range(size+2): # 0=void, 1=blank, 2=solution, 3=dead ends
        cells.append(0)
    for i in range(size):
        cells.append(0)
        for j in range(size):
            cells.append(1)
        cells.append(0)
    for i in range(size+2):
        cells.append(1)

def coordinates(): # translates Cartesian coordinates into cell coordinates
    return int(((size+2)*(ycor()+200+(unit/2))/unit)+((xcor()+200+(3*unit/2))/unit))

def move(): # make one move
    global size
    directions = [0,0,90,90,180,270]
    offsets = [1,size+2,-1,-size-2,0]
    heading = 360
    new_state = cells[coordinates()+offsets[int(heading/90)]] 
    while len(directions) > 0 and new_state != 1:
        heading = directions[randint(0,len(directions)-1)] # Random direction
        directions.remove(heading) # Since we can't go there, remove that.
        if heading < 100: # 0 and 90 occur twice for a NE bias
            directions.remove(heading)
    if len(directions) == 0: # We have gotten into a dead end
        cells[coordinates()] = 3 # 3 is a dead end
        visited.remove(visited[len(visited)-2]) # Remove the last element
        goto(visited[len(visited)-1]) # Goto the new last element
    else:
        seth(heading)
        fd(unit)
        cells[coordinates()] = 2
        visited.append((xcor(),ycor()))

def solution(): # make the trail that leads to the solution
    pencolor('white')
    width(unit/2.0)
    pendown()
    while True:
        try:
            move()
        except:
            break
          
def maze(): # make the maze
    initialize()
    create_array()
    solution()

maze()
