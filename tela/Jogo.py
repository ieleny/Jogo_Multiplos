import pygame
from pygame.locals import *
from random import *
from .CoresModel import CoresModel

class Jogo:
    
    def __init__(self, TELA):
        self.TELA = TELA

    def telaDoJogo(self):

        # Primeira Torre
        self.gerarTorresVerticais(100, 180)

        # Segunda Torre
        self.gerarTorresVerticais(400, 480)

        # Terceira Torre
        self.gerarTorresVerticais(700, 780)

        # Torre horizontal
        pygame.draw.rect(self.TELA, (0, 0, 0, 0), [100, 470, 750, 100])
        self.gerarBolasHorizontal(190,520,40)

        pygame.display.flip()

    def gerarTorresVerticais(self, X_RECT, X_BOLAS):
        
        pygame.draw.rect(
            self.TELA, 
            (0, 0, 0, 0), 
            [X_RECT, 50, 150, 400]
        )
        
        self.gerarBolasVertical(X_BOLAS, 120, 50)

    def gerarBolasVertical(self, X, Y, diametro):
        
        for item in range(5):
            # TODO: Quando clicar irá adicionar a bordar verde
            pygame.draw.circle(self.TELA, CoresModel.VERDE, [X, Y], diametro + 5)
            pygame.draw.circle(self.TELA, CoresModel.VERMELHO, [X, Y], diametro)

            self.TELA.blit(
                pygame.font.SysFont('Comic Sans MS', 40).render(str(randrange(10)), False, (0, 0, 0)),
                (X-10,Y-25)
            )
            Y += 120

    def gerarBolasHorizontal(self, X, Y, diametro):
        
        for item in range(6):
            pygame.draw.circle(
                self.TELA, 
                CoresModel.VERMELHO, 
                [X, Y], 
                diametro
            )
            self.TELA.blit(
                pygame.font.SysFont('Comic Sans MS', 40).render(str(randrange(10)), False, (0, 0, 0)),
                (X-10,Y-25)
            )
            X += 120
