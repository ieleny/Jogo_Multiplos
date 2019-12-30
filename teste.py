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

---------------------------------------------------------------------------------------------------------

import pygame


pygame.init()
width, height = (200,300)
screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)
FONT = pygame.font.Font("freesansbold.ttf", 50)


def loop():
    clock = pygame.time.Clock()
    number = 0
    # The button is just a rect.
    button = pygame.Rect(0, 100, 200, 200)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if button.collidepoint(event.pos):
                        # Increment the number.
                        number += 1

        screen.fill(WHITE)
        pygame.draw.rect(screen, GRAY, button)
        text_surf = FONT.render(str(number), True, BLACK)
        # You can pass the center directly to the `get_rect` method.
        text_rect = text_surf.get_rect(center=(width/2, 30))
        screen.blit(text_surf, text_rect)
        pygame.display.update()

        clock.tick(30)


loop()
pygame.quit()

-----------------------------------------------------------------------------------------------------------------
#import tela.Tela
#pygame = tela.Tela()

import pygame
import sys
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600, 400), 0, 32)
        self.screen.fill((white))
        pygame.display.update()

    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100),
                                     2)
        pygame.display.update()

    def addText(self):
        self.screen.blit(self.font.render('Hello!', True, black), (200, 100))
        pygame.display.update()

    def addText2(self):
        self.screen.blit(self.font.render('Hello!', True, red), (200, 100))
        pygame.display.update()

    def functionApp(self):
        if __name__ == '__main__':
            self.addRect()
            self.addText()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.screen.fill(white)
                            self.addRect()
                            self.addText2(
                            )  #i made it so it only changes colour once.


display = Pane()
display.functionApp()

----------------------------------------------------------------------------------------------------------

import pygame
from pygame.locals import *

def sub_rect(r1, r2):
    """remove the area of r2 from r1"""
    if not r1.colliderect(r2):
        return [r1]

    clip = r2.clip(r1)

    #first we have to see if there is a complete rect to each side of the removing rect
    need_com_left = False
    need_com_right = False
    need_com_top = False
    need_com_bottom = False

    if clip.left > r1.left:
        need_com_left = True
    if clip.right &lt; r1.right:
        need_com_right = True
    if clip.top > r1.top:
        need_com_top = True
    if clip.bottom &lt; r1.bottom:
        need_com_bottom = True

    left = None
    right = None
    top = None
    bottom = None

    if need_com_left: #ok, we also need to check top and bottom here...
        t = r1.top
        b = r1.bottom - r1.top
        l = r1.left
        r = clip.left - r1.left
        if need_com_top: #we need to cut a bit off the top of this
            t = clip.top
        if need_com_bottom:
            b = clip.bottom - t

        left = pygame.Rect(l, t, r, b)
    if need_com_right:
        t = r1.top
        b = r1.bottom - r1.top
        l = clip.right
        r = r1.right - clip.right
        if need_com_top:
            t = clip.top
        if need_com_bottom:
            b = clip.bottom - t

        right = pygame.Rect(l, t, r, b)
    if need_com_top:
        top = pygame.Rect(r1.left, r1.top, r1.width, clip.top-r1.top)
    if need_com_bottom:
        bottom = pygame.Rect(r1.left, clip.bottom, r1.width, r1.bottom-clip.bottom)

    ret = []
    for i in [left, right, top, bottom]:
        if i: ret.append(i)

    return ret

def sub_rect_list(r1, rl):
    dirty = [r1]
    for i in rl:
        new = []
        for x in dirty:
            new.extend(sub_rect(x, i))
        dirty = new
    return dirty

#test this!
a = pygame.Rect(0,0,100,100)
b = pygame.Rect(10,10,80,80)
c = pygame.Rect(80,80,20,20)

dirty = sub_rect_list(a, [b, c])

pygame.init()
screen = pygame.display.set_mode((640, 480))

back = pygame.Surface(a.size)
back.fill((0,255,0))

screen.blit(back, (0,0))

new = pygame.Surface(a.size)
new.fill((255,0,0))

for i in dirty:
    if i:
        screen.blit(new, i.topleft, i)
pygame.display.flip()