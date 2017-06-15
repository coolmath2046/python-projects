import pygame,time,random

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
draw = pygame.draw
clock = pygame.time.Clock()
PEACH = (255,196,160)
BLUE = (0,158,238)
ORANGE = (255,100,0)
BLACK = (0,0,0)
XSTART = 30
YSTART = 40
SPEED = 5

while not done:
    clock.tick(60)
    screen.fill(PEACH)
    for event in pygame.event.get(): # Event handling loop
        if event.type == pygame.QUIT:
            done = True
        SPACE = (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)
        LEFT = (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT)
        RIGHT = (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT)
        UP = (event.type == pygame.KEYDOWN and event.key == pygame.K_UP)
        DOWN = (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN)

    draw.rect(screen,BLACK,pygame.Rect(170,120,60,60)) # Goal-box
    # Start of event if-statements
    if SPACE: # Check to see if space is pressed
        draw.rect(screen,ORANGE,pygame.Rect(XSTART,-YSTART,60,60))
##    else:
##        draw.rect(screen,PEACH,pygame.Rect(XSTART,-YSTART,60,60))
    if LEFT: XSTART -= SPEED
    if RIGHT: XSTART += SPEED
    if UP: YSTART += SPEED
    if DOWN: YSTART -= SPEED
    pygame.display.flip()
