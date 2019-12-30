import pygame, sys
from pygame.locals import *


class Jogo:
    def __init__(self, TELA, X, Y):

        self.TELA = TELA
        self.X = X
        self.Y = Y

    def telaDoJogo(self):

        #Primeira Torre
        font_button = pygame.font.Font('freesansbold.ttf', 50)
        pygame.draw.rect(self.TELA, self.AZUL,
                         (self.X // 3, self.Y // 2.5, 300, 70))
        text = font_button.render('Jogar', True, self.VERDE)
        textRect = text.get_rect()
        textRect.center = (self.X // 2.1, self.Y // 2.2)
        self.TELA.blit(text, textRect)