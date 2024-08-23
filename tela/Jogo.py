import pygame
from pygame.locals import *
from random import *
from .CoresModel import CoresModel
from .ModeloTorresVerticais import ModeloTorresVerticais

class Jogo:

    listaBolasClicaveis = []
    ultimaBolaTorre = []

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
        
        pygame.display.update()

    def gerarTorresVerticais(self, X_RECT, X_BOLAS):
        
        pygame.draw.rect(
            self.TELA, 
            (0, 0, 0, 0), 
            [X_RECT, 50, 150, 400]
        )
        
        self.gerarBolasVertical(X_BOLAS, 120, 40)

    def gerarBolasVertical(self, X, Y, diametro):
        
        for item in range(3):

            NUMERO_ATUAL = str(randrange(10))

            modeloTorresVerticais = ModeloTorresVerticais(1, NUMERO_ATUAL, X, Y)

            self.ultimaBolaTorre.append(modeloTorresVerticais)
            self.listaBolasClicaveis.append(pygame.Rect(X, Y, 300, 300))

            pygame.draw.circle(self.TELA, CoresModel.VERMELHO, [X, Y], diametro)
            self.TELA.blit(
                pygame.font.SysFont('Comic Sans MS', 40).render(NUMERO_ATUAL, False, (0, 0, 0)),
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

    def cliqueBolas(self, event):
        for item in range(9):
            # Verifica se a posição é do botão
            if self.listaBolasClicaveis[item].collidepoint(event.pos):
                # Transformar em um dicionário
                print(self.ultimaBolaTorre[item].Largura, self.ultimaBolaTorre[item].Altura)

                # TODO: Quando clicar irá adicionar a borda verde
                pygame.draw.circle(self.TELA, CoresModel.VERDE, [self.ultimaBolaTorre[item].Altura, self.ultimaBolaTorre[item].Largura], 55)
                pygame.display.flip()