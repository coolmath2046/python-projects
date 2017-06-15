import pygame,statistics
from random import randint
pygame.init()

# Space to make a map, s to save, l to load, any other key to do next iteration
# Maps 12 to 69 are for the Susababerry Evolution Simulator

SCREENX = 1320
SCREENY = 840
TILE = 20
MAPSIZE = int((SCREENX*SCREENY)/(TILE**2))
LENGTH = int(SCREENX/TILE)
HEIGHT = int(SCREENY/TILE)
MIN_ELEV = -5000
MAX_ELEV = 5100
ITERATIONS = 2
DO_ITERATIONS = True
RESPONSE = False # For this to work, switch to True. For the Susababerry Evolution Simulator to work, switch to False.
SWATH = 2 # This variable adjusts the size of 'influence' each cell has.

the_map = [[y for y in range(HEIGHT)] for x in range(LENGTH)]
display = pygame.display
screen = display.set_mode((SCREENX,SCREENY))
max_elev = MAX_ELEV

def land_color(elevation):
    if elevation < 0:
        return (0,0,0)
    elif elevation > max_elev/2:
        return (255,max(0,(max_elev-elevation)/(max_elev/510)),0)
    else:
        return (max(0,(elevation/(max_elev/510))),255,0)

def createmap(MIN_ELEV,max_elev):
    for x in range(0,SCREENX,TILE):
        for y in range(0,SCREENY,TILE):
            the_map[int(x/TILE)][int(y/TILE)] = randint(MIN_ELEV,max_elev)
            
def drawmap():
    def find2d(matrix,value):
        return [(index, row.index(value)) for index, row in enumerate(matrix) if value in row][0]
    for x in range(0,SCREENX,TILE):
        for y in range(0,SCREENY,TILE):
            elevation = int(the_map[int(x/TILE)][int(y/TILE)])
            screen.fill(land_color(elevation),(x,y,TILE,TILE))
    display.update()

def refinemap():
    global the_map
    tempmap = the_map
    for x in range(0,LENGTH):
        for y in range(0,HEIGHT):
            neighbors = []
            [[neighbors.append((i,j)) for i in range(x-SWATH,x+SWATH+1) if (i >= 0 and i < LENGTH and j >= 0 and j < HEIGHT)] for j in range(y-SWATH,y+SWATH+1)]
            tempmap[x][y] = int(statistics.mean([the_map[i[0]][i[1]] for i in neighbors]))
    the_map = tempmap
    
def makemap():
    global max_elev,the_map
    max_elev = MAX_ELEV
    the_map = [[y for y in range(HEIGHT)] for x in range(LENGTH)]
    createmap(MIN_ELEV,max_elev)
    drawmap()
    if DO_ITERATIONS:
        for i in range(ITERATIONS):
            print('Iteration '+str(i))
            refinemap()
            drawmap()
            max_elev = max(max(the_map))

def loadmap(code):
    global the_map,max_elev,SCREENX,SCREENY,TILE    
    master = code.split('g')
    SCREENX = int(master[0])
    SCREENY = int(master[1])
    TILE = int(master[2])
    code = master[3]
    screen = display.set_mode((SCREENX,SCREENY))
    def str_to_list(string):
        list_sep = 'n'
        val_sep = ','
        string = string.split(list_sep)
        for i in enumerate(string):
            string[i[0]] = i[1].split(val_sep)
        return [[int(i) for i in j] for j in string]
    the_map = str_to_list(code)
    max_elev = max(max(the_map))
    drawmap()
    return the_map

def savemap():
    def list_to_str(t):
        string = ''
        for sublist in t:
            for element in sublist:
                string += str(element) + ','
            string = string[:-1]
            string += 'n'
        return string[:-1]    
    open('mapcode.txt','a').write(str(SCREENX)+'g'+str(SCREENY)+'g'+str(TILE)+'g'+list_to_str(the_map)+' ')
    print('The map ID is: '+str(len(open('mapcode.txt','r').read().split())-1))

while RESPONSE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                makemap()
            elif event.key == pygame.K_s:
                savemap()
            elif event.key == pygame.K_l:
                maps = open('mapcode.txt','r').read().split()
                print('There are '+str(len(maps))+' available from 0 to '+str(len(maps)-1))
                loadmap(maps[int(input('Which map do you want to load? Map ID: '))])
            else:
                refinemap()
                drawmap()
                max_elev = max(max(the_map))                
