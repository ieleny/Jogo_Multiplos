import pygame, sys
from pygame.locals import *


class Jogo:

    #Constante
    VERMELHO = (125, 0, 0)

    def __init__(self, TELA, X, Y):

        self.TELA = TELA
        self.X = X
        self.Y = Y

    def telaDoJogo(self):

        #Primeira Torre
        pygame.draw.rect(self.TELA, (0, 0, 0, 0), [100, 50, 150, 400])
        self.gerarNumeros(170, 120, 50)

        #Segunda Torre
        pygame.draw.rect(self.TELA, (0, 0, 0, 0), [400, 50, 150, 400])

        #Terceira Torre
        pygame.draw.rect(self.TELA, (
            0,
            0,
            0,
        ), [700, 50, 150, 400])

        #Torre horizontal
        pygame.draw.rect(self.TELA, (0, 0, 0, 0), [100, 470, 750, 100])

        pygame.display.flip()

    def gerarNumeros(self, X, Y, diamentro):

        for item in range(3):
            print(item)
            pygame.draw.circle(self.TELA, self.VERMELHO, [X, Y], diamentro)
            Y += 120