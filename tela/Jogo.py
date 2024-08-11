import pygame, sys
from pygame.locals import *
from random import *

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
        self.gerarBolasVertical(180, 120, 50)

        #Segunda Torre
        pygame.draw.rect(self.TELA, (0, 0, 0, 0), [400, 50, 150, 400])
        self.gerarBolasVertical(480, 120, 50)

        #Terceira Torre
        pygame.draw.rect(self.TELA, (
            0,
            0,
            0,
        ), [700, 50, 150, 400])
        self.gerarBolasVertical(780, 120, 50)

        #Torre horizontal
        pygame.draw.rect(self.TELA, (0, 0, 0, 0), [100, 470, 750, 100])
        self.gerarBolasHorizontal(190,520,40)

        pygame.display.flip()

    def gerarBolasVertical(self, X, Y, diametro):

        for item in range(3):
            pygame.draw.circle(self.TELA, self.VERMELHO, [X, Y], diametro)
            self.TELA.blit(
                pygame.font.SysFont('Comic Sans MS', 40).render(str(randrange(10)), False, (0, 0, 0)),
                (X-10,Y-25)
            )
            Y += 120

    def gerarBolasHorizontal(self, X, Y, diametro):

        for item in range(6):
            pygame.draw.circle(self.TELA, self.VERMELHO, [X, Y], diametro)
            self.TELA.blit(
                pygame.font.SysFont('Comic Sans MS', 40).render(str(randrange(10)), False, (0, 0, 0)),
                (X-10,Y-25)
            )
            X += 120