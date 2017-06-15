from turtle import *
from random import *

size = 5 # the size of the maze

# initialize
delay(5)
speed(5)
#hideturtle()

# glides to a certain position without making a mark
def glide(x,y):
    penup()
    goto(x,y)
    pendown()

def square():
    glide(-200-600/size,200+600/size)
    begin_fill()
    for z in range(4):
        fd(400+1200/size)
        rt(90)
    end_fill()

def dot():
    pendown()
    fd(0.25)
    bk(0.25)

def travel(index):
    goto((400/(size-1))*(cell%size)-200,(400/(size-1))*(int(cell%size))-200)

square()

width(360/size)
pencolor('white')
visited = [0-size,-1,size**2+size,size**2+1]
alive = []
guide = [1,0-size,-1,size]

# go to the 'hub'
if size%2 == 1:
    glide(0,0)
    visited.append(int((size**2-1)/2))
    alive.append(int((size**2-1)/2))
else:
    glide(200/(size-1),200/(size-1))
    visited.append(int((size**2-size)/2))
    alive.append(int((size**2-size)/2))

while True:
    print(visited)
    print(alive)
    # check for dead cells

    for cell in alive:
        if cell%size == 0: # left edge
            if cell-size in visited and cell+1 in visited and cell+size in visited:
                alive.remove(cell)
        elif cell%size == size-1: # right edge
            if cell-size in visited and cell-1 in visited and cell+size in visited:
                alive.remove(cell)
        elif cell < size: # top edge
            if cell+size in visited and cell-1 in visited and cell+1 in visited:
                alive.remove(cell)
        elif cell > size**2-size-1: # bottom edge
            if cell-size in visited and cell-1 in visited and cell+1 in visited:
                alive.remove(cell)
        else: # center cells
            if cell+size in visited and cell-size in visited and cell-1 in visited and cell+1 in visited:
                alive.remove(cell)

    # choose a random live cell and make a branch

    cell = alive[randint(0,len(alive)-1)]
    direction = randint(0,3)
    glide((400/(size-1))*(cell%size)-200,(400/(size-1))*(int(cell%size))-200)
    seth(90*direction)
    if cell+guide[direction] not in visited and cell+guide[direction] >= -1 and cell+guide[direction] < size**2 and abs((cell%size)-((cell+guide[direction])%size)) != size-1:
        fd(400/(size-1))
        visited.append(cell+guide[direction])
        alive.append(cell+guide[direction])
        




        







