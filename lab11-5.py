import pygame, sys

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 400))

original_image = pygame.image.load("roulette.png")
rect = original_image.get_rect()
rect.center = (200, 200)
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rotated_image = pygame.transform.rotate(original_image, angle)
    angle += 30 % 360

    rect = rotated_image.get_rect()
    rect.center = (200, 200)

    screen.fill((225,225,225,))
    screen.blit(rotated_image, rect)

    pygame.display.update()
    fpsClock.tick(FPS)
