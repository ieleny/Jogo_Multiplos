import pygame
from pygame.locals import *
from random import *
from .CoresModel import CoresModel
from .ModeloTorres import ModeloTorres

class Jogo:

    # Salvar dos objetos clicaveis - Vertical
    listaBolasClicaveisVerticais = []
    bolasVerticais = []

    # Salvar os objetos clicaveis - Horizontais
    listaBolasClicaveisHorizontais = []
    bolasHorizontais = []

    # Salvar a soma dos valores
    somaValores = 0

    # Salvar a pontuação do jogo
    pontuacao = 0

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

            NUMERO_ATUAL = str(randrange(1, 10))

            if item == 2:
                modeloTorresVerticais = ModeloTorres('vertical', NUMERO_ATUAL, X, Y)
                self.bolasVerticais.append(modeloTorresVerticais)
                # pygame.rect defini o local que o valor poderá ser clicado
                self.listaBolasClicaveisVerticais.append(pygame.Rect(X-40, Y-40, 80, 80))

            pygame.draw.circle(self.TELA, CoresModel.VERMELHO, [X, Y], diametro)
            self.TELA.blit(
                pygame.font.SysFont('Comic Sans MS', 40).render(NUMERO_ATUAL, False, (0, 0, 0)),
                (X-10,Y-25)
            )

            Y += 120

    def gerarBolasHorizontal(self, X, Y, diametro):

        for item in range(6):

            NUMERO_ATUAL = str(randrange(1, 10))

            modeloTorresHorizonais = ModeloTorres('horizontal', NUMERO_ATUAL, X, Y)
            self.bolasHorizontais.append(modeloTorresHorizonais)
            self.listaBolasClicaveisHorizontais.append(pygame.Rect(X, Y, 300, 300))

            pygame.draw.circle(
                self.TELA, 
                CoresModel.VERMELHO, 
                [X, Y], 
                diametro
            )

            self.TELA.blit(
                pygame.font.SysFont('Comic Sans MS', 40).render(NUMERO_ATUAL, False, (0, 0, 0)),
                (X-10,Y-25)
            )

            X += 120

    def cliqueBolas(self, event):

        if self.listaBolasClicaveisVerticais[0].collidepoint(event.pos):
            self.gerarTextoCliqueBolas(0)

        if self.listaBolasClicaveisVerticais[1].collidepoint(event.pos):
            self.gerarTextoCliqueBolas(1)
        
        if self.listaBolasClicaveisVerticais[2].collidepoint(event.pos):
            self.gerarTextoCliqueBolas(2)

    def gerarTextoCliqueBolas(self, index):
        pygame.draw.circle(
                        self.TELA, 
                        CoresModel.VERDE, 
                        [self.bolasVerticais[index].EixoX, self.bolasVerticais[index].EixoY], 
                        45
        )
        pygame.draw.circle(
            self.TELA, 
            CoresModel.VERMELHO, 
            [self.bolasVerticais[index].EixoX, self.bolasVerticais[index].EixoY], 
            40
        )
        self.TELA.blit(
            pygame.font.SysFont('Comic Sans MS', 40).render(str(self.bolasVerticais[index].NumeroBola), False, (0, 0, 0)),
            (self.bolasVerticais[index].EixoX - 10, self.bolasVerticais[index].EixoY - 25)
        )

        self.gerarTextoSomaValores(self.bolasVerticais[index].NumeroBola)

    def gerarTextoSomaValores(self, valor):

        font = pygame.font.SysFont('Comic Sans MS', 35)

        print("1", self.somaValores + 1)

        self.somaValores += int(valor)

        print("2", self.somaValores)
        
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