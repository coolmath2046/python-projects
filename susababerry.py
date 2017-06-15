from map import * # You must go into map.py and switch RESPONSE to False
from random import randint,random
import pygame, time, sys

pygame.init()
sys.setrecursionlimit(15000)

LENGTH = 66
HEIGHT = 42
MINMAP = 12
MAXMAP = 75
TILE = 20
SCREENX = LENGTH*TILE
SCREENY = HEIGHT*TILE
STARTINGSUSABAPROB = 1 #0.02
SUSABACOL = (0,0,255)

regionSize = 0
berryNum = 0

def load_random_map():
    maps = open('mapcode.txt','r').read().split()
    random_map = randint(MINMAP,MAXMAP)
    the_map = loadmap(maps[random_map])
    return susababerries(the_map),the_map

def susababerries(the_map):
    def sign(num):
        if num < 0:
            return -1
        else:
            return 1
    def floodFill(mapObj,x,y,oldCharacter,newCharacter):
        global regionSize,berryNum
        regionSize += 1
        if mapObj[x][y] == oldCharacter:
            mapObj[x][y] = newCharacter
            susabaprob = STARTINGSUSABAPROB*(1-(the_map[x][y]/max(max(the_map))))
            if random() < susabaprob:
                mapObj[x][y] = 3 # August 3 is National Susababerry Day!
                berryNum += 1
                screen.fill(SUSABACOL,(x*TILE,y*TILE,TILE,TILE))
                display.update()
        if x < LENGTH - 1 and mapObj[x+1][y] == oldCharacter:
            floodFill(mapObj, x+1, y, oldCharacter, newCharacter) # call right
        if x > 0.5 and mapObj[x-1][y] == oldCharacter:
            floodFill(mapObj, x-1, y, oldCharacter, newCharacter) # call left
        if y < HEIGHT - 1 and mapObj[x][y+1] == oldCharacter:
            floodFill(mapObj, x, y+1, oldCharacter, newCharacter) # call down
        if y > 1 and mapObj[x][y-1] == oldCharacter:
            floodFill(mapObj, x, y-1, oldCharacter, newCharacter) # call up
        return regionSize
    
    def find_random_land():
        global regionSize
        randX = randint(0,LENGTH-1)
        randY = randint(0,HEIGHT-1)
        susabastatus = [[sign(the_map[x][y]) for y in range(HEIGHT)] for x in range(LENGTH)]
        regionSize = 0
        while (the_map[randX][randY] < 0) or floodFill(susabastatus,randX,randY,1,2) < 400:
            regionSize = 0
            randX = randint(0,LENGTH-1)
            randY = randint(0,HEIGHT-1)
            susabastatus = [[sign(the_map[x][y]) for y in range(HEIGHT)] for x in range(LENGTH)]
        print('Susababeri Count: '+str(berryNum))
        screen.fill(SUSABACOL,(randX*TILE,randY*TILE,TILE,TILE))
        display.update()
        return (randX,randY)
    return find_random_land()

def simulate():
    # Note: In this function, I will repeatedly use return to mark the end.
    global berryNum
    berryNum = 1
    pos = load_random_map()
    creatureX = pos[0][0]*TILE
    creatureY = pos[0][1]*TILE
    the_map = pos[1]
    prev_sq = (creatureX,creatureY)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    prev_sq = (creatureX,creatureY)
                    creatureY -= TILE
                if event.key == pygame.K_DOWN:
                    prev_sq = (creatureX,creatureY)
                    creatureY += TILE
                if event.key == pygame.K_LEFT:
                    prev_sq = (creatureX,creatureY)
                    creatureX -= TILE
                if event.key == pygame.K_RIGHT:
                    prev_sq = (creatureX,creatureY)
                    creatureX += TILE
                if event.key == pygame.K_n:
                    simulate()
        if creatureX < 0 or creatureX > SCREENX or creatureY < 0 or creatureY > SCREENY:
            return  # Oh no, out of bounds
        if the_map[int(creatureX/TILE)][int(creatureY/TILE)] < 0:
            return  # Oh no, underwater
        screen.fill(land_color(the_map[int(prev_sq[0]/TILE)][int(prev_sq[1]/TILE)]),(prev_sq[0],prev_sq[1],TILE,TILE))
        screen.fill((255,0,255),(creatureX,creatureY,TILE,TILE))
        display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                berryNum = 1
                load_random_map()
            if event.key == pygame.K_n:
                simulate()
                screen.fill((0,0,0))
                display.update()
