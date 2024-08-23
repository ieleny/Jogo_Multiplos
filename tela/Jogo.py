import pygame
from pygame.locals import *
from random import *
from .CoresModel import CoresModel
from .ModeloTorresVerticais import ModeloTorresVerticais

class Jogo:

    # Salvar os dados
    listaBolasClicaveis = []
    bolasVerticais = []

    # Estudar raio e circuferência para saber qual o centro da bola

    def __init__(self, TELA):
        self.TELA = TELA

    def telaDoJogo(self):

        # Primeira torre vertical
        self.gerarTorresVerticais(100, 180)

        # Segunda torre vertical
        self.gerarTorresVerticais(400, 480)

        # Terceira torre vertical
        self.gerarTorresVerticais(700, 780)

        # Torre horizontal
        pygame.draw.rect(self.TELA, (0, 0, 0, 0), [100, 470, 750, 100])
        self.gerarBolasHorizontal(190,520,40)

        # Texto de pontução
        self.TELA.blit(
            pygame.font.SysFont('Comic Sans MS', 40).render("Pontuação", False, (0, 0, 0)),
            (700,100)
        )

        # Texto da soma dos valores
        self.TELA.blit(
            pygame.font.SysFont('Comic Sans MS', 40).render("Soma dos valores", False, (0, 0, 0)),
            (700,200)
        )
        
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

            self.bolasVerticais.append(modeloTorresVerticais)
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
            # Verifica se a posição é do botão
            if self.listaBolasClicaveis[2].collidepoint(event.pos):
                pygame.draw.circle(self.TELA, CoresModel.VERDE, [self.bolasVerticais[2].Altura, self.bolasVerticais[2].Largura], 45)
                pygame.draw.circle(
                    self.TELA, 
                    CoresModel.VERMELHO, 
                    [self.bolasVerticais[2].Altura, self.bolasVerticais[2].Largura], 
                    40
                )
                self.TELA.blit(
                    pygame.font.SysFont('Comic Sans MS', 40).render(str(self.bolasVerticais[2].NumeroBola), False, (0, 0, 0)),
                    (self.bolasVerticais[2].Altura - 10, self.bolasVerticais[2].Largura - 25)
                )

            if self.listaBolasClicaveis[5].collidepoint(event.pos):
                pygame.draw.circle(self.TELA, CoresModel.VERDE, [self.bolasVerticais[5].Altura, self.bolasVerticais[5].Largura], 45)
                pygame.draw.circle(
                    self.TELA, 
                    CoresModel.VERMELHO, 
                    [self.bolasVerticais[5].Altura, self.bolasVerticais[5].Largura], 
                    40
                )
                self.TELA.blit(
                    pygame.font.SysFont('Comic Sans MS', 40).render(str(self.bolasVerticais[5].NumeroBola), False, (0, 0, 0)),
                    (self.bolasVerticais[5].Altura - 10, self.bolasVerticais[5].Largura - 25)
                )
            
            if self.listaBolasClicaveis[8].collidepoint(event.pos):
                pygame.draw.circle(self.TELA, CoresModel.VERDE, [self.bolasVerticais[8].Altura, self.bolasVerticais[8].Largura], 45)
                pygame.draw.circle(
                    self.TELA, 
                    CoresModel.VERMELHO, 
                    [self.bolasVerticais[8].Altura, self.bolasVerticais[8].Largura], 
                    40
                )
                self.TELA.blit(
                    pygame.font.SysFont('Comic Sans MS', 40).render(str(self.bolasVerticais[8].NumeroBola), False, (0, 0, 0)),
                    (self.bolasVerticais[8].Altura - 10, self.bolasVerticais[8].Largura - 25)
                )