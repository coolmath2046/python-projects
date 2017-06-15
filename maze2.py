import pygame, sys
from random import *

WINWIDTH = 800
WINHEIGHT = 800
GRIDWIDTH = 40
GRIDHEIGHT = 40
TILEWIDTH = WINWIDTH/GRIDWIDTH
TILEHEIGHT = WINHEIGHT/GRIDHEIGHT
BLACK = (0,0,0)
WHITE = (255,255,255)

maze = [[BLACK for y in range(GRIDHEIGHT)] for x in range(GRIDWIDTH)]
pygame.init()
display = pygame.display
screen = display.set_mode((WINHEIGHT,WINWIDTH))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
