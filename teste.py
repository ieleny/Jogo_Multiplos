import pygame, sys
from pygame.locals import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
DISPLAYSURF.fill(WHITE)
SPAMRECT = (10, 20, 100, 100)
pygame.draw.rect(DISPLAYSURF, RED, SPAMRECT)

pygame.display.set_caption('Multiplo 5')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()