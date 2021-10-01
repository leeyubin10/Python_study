import pygame, sys
from pygame.locals import*

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('테두리 따라 움직이기')

WHITE = (255,255,255)
balling = pygame.image.load('ball.png')

ballx = 10
bally = 10
direction = 'right'

while True:
    screen.fill(WHITE)
    if direction == 'right':
        ballx += 5
        if ballx == 280:
            direction = 'down'
    elif direction == 'down':
        bally += 5
        if bally == 190:
            direction = 'left'
    elif direction == 'left':
        ballx -= 5
        if ballx == 0:
            direction = 'up'
    elif direction == 'up':
        bally -= 5
        if bally == 10:
            direction = 'right'

    screen.blit(balling, (ballx,bally))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
