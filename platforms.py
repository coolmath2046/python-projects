import pygame

GREEN = (23,157,9)
GRAY = (130,130,130)
BLACK = (0,0,0)
RED = (255,0,16)
BLUE = (0,74,255)
YELLOW = (241,239,0)

SCREENX = 1000
SCREENY = 700

RECTANGLES = {(0,SCREENY-100,SCREENX,100):GRAY,(100,500,300,50):GREEN}

SIZE = 40 # Player's size
STEP = 3
playerX = 15
playerY = SCREENY - 100 - SIZE

display = pygame.display
pygame.init()
screen = display.set_mode((SCREENX,SCREENY))

def isIntersecting(rect1,rect2):
    return colliderect
def draw():
    screen.fill(BLACK)
    screen.fill(YELLOW,(playerX,playerY,SIZE,SIZE))
    [screen.fill(RECTANGLES[r],r) for r in RECTANGLES]
    display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: playerY -= STEP
    if pressed[pygame.K_DOWN]: playerY += STEP
    if pressed[pygame.K_LEFT]: playerX -= STEP
    if pressed[pygame.K_RIGHT]: playerX += STEP
    draw()
                
            
