import pygame
from pygame.locals import *
from random import *
from .CoresModel import CoresModel
from .ModeloTorresVerticais import ModeloTorresVerticais

class Jogo:

    # Salvar dos objetos clicaveis
    listaBolasClicaveis = []
    bolasVerticais = []

    # Salvar a pontuação
    somaValores = 0

    # Eixos
    dicionarioTorres =   { 
                            'primeiraTorreVertical': { 'eixoXTorre': 100, 'eixoXBolas': 180 },
                            'segundaTorreVertical':  { 'eixoXTorre': 330, 'eixoXBolas': 410 },
                            'terceiraTorreVerical': { 'eixoXTorre': 560, 'eixoXBolas': 640 },
                            'torreHorizontal': { 'eixoXTorre': 100, 'eixoXBolas': 190 }
                        }

    # Estudar raio e circuferência para saber qual o centro da bola, para colocar o número

    def __init__(self, TELA):
        self.TELA = TELA

    def telaDoJogo(self):

        # Primeira torre vertical
        self.gerarTorresVerticais(
                                    self.dicionarioTorres['primeiraTorreVertical']['eixoXTorre'], 
                                    self.dicionarioTorres['primeiraTorreVertical']['eixoXBolas']
                                )

        # Segunda torre vertical
        self.gerarTorresVerticais(
                                    self.dicionarioTorres['segundaTorreVertical']['eixoXTorre'], 
                                    self.dicionarioTorres['segundaTorreVertical']['eixoXBolas']
                                )

        # Terceira torre vertical
        self.gerarTorresVerticais(
                                    self.dicionarioTorres['terceiraTorreVerical']['eixoXTorre'], 
                                    self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas']
                                )

        # Torre horizontal
        self.gerarTorresHorizontais(  
                                    self.dicionarioTorres['torreHorizontal']['eixoXTorre'], 
                                    self.dicionarioTorres['torreHorizontal']['eixoXBolas']
                                )


        # Texto de pontução
        self.TELA.blit(
            pygame.font.SysFont('Comic Sans MS', 35).render("Pontuação:", False, (0, 0, 0)),
            (self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas'] + 100, 100)
        )

        # Texto da soma dos valores
        self.TELA.blit(
            pygame.font.SysFont('Comic Sans MS', 35).render("Soma dos valores:", False, (0, 0, 0)),
            (self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas'] + 100, 200)
        )
    

    def gerarTorresVerticais(self, X_RECT, X_BOLAS):
        
        pygame.draw.rect(
            self.TELA, 
            (0, 0, 0, 0), 
            [X_RECT, 50, 150, 400]
        )
        
        self.gerarBolasVertical(X_BOLAS, 120, 40)

    def gerarTorresHorizontais(self, X_RECT, X_BOLAS):
        
        pygame.draw.rect(
            self.TELA, 
            (0, 0, 0, 0), 
            [X_RECT, 470, 750, 100]
        )
    
        self.gerarBolasHorizontal(X_BOLAS, 520, 40)

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

                self.gerarTextoSomaValores(int(self.bolasVerticais[2].NumeroBola))

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

                self.gerarTextoSomaValores(int(self.bolasVerticais[5].NumeroBola))
            
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

                self.gerarTextoSomaValores(int(self.bolasVerticais[8].NumeroBola))

    def gerarTextoSomaValores(self, valor):

        font = pygame.font.SysFont('Comic Sans MS', 35)
        self.somaValores = int(self.somaValores) + int(valor)
        
        # Texto da soma dos valores
        pygame.draw.circle(
            self.TELA, 
            CoresModel.BRANCO, 
            (self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas'] + 120, 280), 
            40
        )
        self.TELA.blit(
            font.render(str(self.somaValores), False, (0, 0, 0)),
            (self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas'] + 100, 250)
        )