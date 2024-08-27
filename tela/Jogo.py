import pygame
from pygame.locals import *
from random import *
from .CoresModel import CoresModel
from .ModeloTorres import ModeloTorres

class Jogo:

    # Salvar dos objetos clicaveis - Vertical
    listaOrbesClicaveisVerticais = []
    orbesVerticais = []

    # Salvar os objetos clicaveis - Horizontais
    listaOrbesClicaveisHorizontais = []
    orbesHorizontais = []

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
        
        for index in range(3):

            NUMERO_ATUAL = str(randrange(1, 10))

            # Só salvar se o index for 2, que significa que é o última orbe da torre
            if index == 2:
                # Salvar o objeto da torre vertical com seus dados, do número atual, eixo x e eixo y
                modeloTorresVerticais = ModeloTorres('vertical', NUMERO_ATUAL, X, Y)
                self.orbesVerticais.append(modeloTorresVerticais)
                # pygame.rect defini o local que o valor poderá ser clicado
                self.listaOrbesClicaveisVerticais.append(pygame.Rect(X-40, Y-40, 80, 80))

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
            self.orbesHorizontais.append(modeloTorresHorizonais)
            self.listaOrbesClicaveisHorizontais.append(pygame.Rect(X - 40, Y - 40, 80, 80))

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

    def cliqueOrbes(self, event):
        # Compara se a orbe vertical, está no mesmo ponto que o mouse
        if self.listaOrbesClicaveisVerticais[0].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesVerticais[0])

        if self.listaOrbesClicaveisVerticais[1].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesVerticais[1])
        
        if self.listaOrbesClicaveisVerticais[2].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesVerticais[2])

        # Compara se a orbe horizon, está no mesmo ponto que o mouse
        if self.listaOrbesClicaveisHorizontais[0].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesHorizontais[0])
        
        if self.listaOrbesClicaveisHorizontais[1].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesHorizontais[1])
        
        if self.listaOrbesClicaveisHorizontais[2].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesHorizontais[2])
        
        if self.listaOrbesClicaveisHorizontais[3].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesHorizontais[3])
        
        if self.listaOrbesClicaveisHorizontais[4].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesHorizontais[4])
        
        if self.listaOrbesClicaveisHorizontais[5].collidepoint(event.pos):
            self.gerarTextoCliqueOrbes(self.orbesHorizontais[5])

    def gerarTextoCliqueOrbes(self, orbes):
        pygame.draw.circle(
                        self.TELA, 
                        CoresModel.VERDE, 
                        [orbes.EixoX, orbes.EixoY], 
                        45
        )
        pygame.draw.circle(
            self.TELA, 
            CoresModel.VERMELHO, 
            [orbes.EixoX, orbes.EixoY], 
            40
        )
        self.TELA.blit(
            pygame.font.SysFont('Comic Sans MS', 40).render(str(orbes.NumeroBola), False, (0, 0, 0)),
            (orbes.EixoX - 10, orbes.EixoY - 25)
        )

        self.gerarTextoSomaValores(orbes.NumeroBola)

    def gerarTextoSomaValores(self, valor):

        font = pygame.font.SysFont('Comic Sans MS', 35)

        self.somaValores += int(valor)
        
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