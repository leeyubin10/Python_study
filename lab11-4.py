import pygame, sys
from pygame.locals import*

pygame.init()

flag = None
FPS = 30
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((400,600),0,32)
pygame.display.set_caption('물체 맞추기')

BLACK = ( 0, 0, 0)
WHITE = (255,255,255)

fontObj = pygame.font.Font(None, 32)
textSurfaceObj = fontObj.render('hit', True, BLACK)
textRectObj = textSurfaceObj.get_rect();
textRectObj.center = (150, 200)

target_img = pygame.image.load('ball.png')
target_rect = target_img.get_rect()
target_size = target_img.get_rect().size

arrow_img = pygame.image.load('arrow.png')
arrow_x = 200
arrow_y = 550

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_SPACE]):
        if arrow_y > 0:
            arrow_y -= 10
        else:
            arrow_y = 500
                
                
    if arrow_y == target_rect.y & arrow_x == target_rect.x:
        screen.blit(textSurfaceObj, textRectObj)
        print('hit')

    if target_rect.x > screen.get_width():
        target_rect.x = 0
    else:
        target_rect.x += 5

        #if event.type == KEYDOWN:
         #   if event.key == K_SPACE:
          #      screen.blit(arrow_img, (arrow_x, arrow_y))

    screen.fill(WHITE)

    screen.blit(target_img, target_rect)
    screen.blit(arrow_img, (arrow_x, arrow_y))

    pygame.display.update()
    fpsClock.tick(FPS)
