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

    # Salvar os objetos que foram marcados
    listaOrbesClicados = []

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
            self.gerarCliqueOrbes(self.orbesVerticais[0])

        if self.listaOrbesClicaveisVerticais[1].collidepoint(event.pos):
            self.gerarCliqueOrbes(self.orbesVerticais[1])
        
        if self.listaOrbesClicaveisVerticais[2].collidepoint(event.pos):
            self.gerarCliqueOrbes(self.orbesVerticais[2])

        # Compara se a orbe horizon, está no mesmo ponto que o mouse
        if self.listaOrbesClicaveisHorizontais[0].collidepoint(event.pos):
            self.gerarCliqueOrbes(self.orbesHorizontais[0])
        
        if self.listaOrbesClicaveisHorizontais[1].collidepoint(event.pos):
            self.gerarCliqueOrbes(self.orbesHorizontais[1])
        
        if self.listaOrbesClicaveisHorizontais[2].collidepoint(event.pos):
            self.gerarCliqueOrbes(self.orbesHorizontais[2])
        
        if self.listaOrbesClicaveisHorizontais[3].collidepoint(event.pos):
            self.gerarCliqueOrbes(self.orbesHorizontais[3])
        
        if self.listaOrbesClicaveisHorizontais[4].collidepoint(event.pos):
            self.gerarCliqueOrbes(self.orbesHorizontais[4])
        
        if self.listaOrbesClicaveisHorizontais[5].collidepoint(event.pos):
            self.gerarCliqueOrbes(self.orbesHorizontais[5])

    def gerarCliqueOrbes(self, orbe):
        font = pygame.font.SysFont('Comic Sans MS', 35)

        # Somar os valores
        self.somaValores += int(orbe.NumeroBola)

        print("--------------------------------------" )
        print("if", len(self.listaOrbesClicados) == 2 and self.somaValores % 5 != 0)
        print("quantidade", len(self.listaOrbesClicados) == 2)
        print("resto", self.somaValores % 5 != 0)
        print("O resto é 0", self.somaValores % 5 == 0)
        print("somaValores", self.somaValores)
        print("--------------------------------------" )

        # Verificar se a listaOrbesClicados tem 3 na lista e o resto da soma de valores
        if len(self.listaOrbesClicados) == 2 and self.somaValores % 5 != 0:
            self.somaValores = 0

            for item in self.listaOrbesClicados:
                pygame.draw.circle(
                    self.TELA, 
                    CoresModel.VERMELHO, 
                    [item.EixoX, item.EixoY], 
                    45
                )
                pygame.draw.circle(
                    self.TELA, 
                    CoresModel.VERMELHO, 
                    [item.EixoX, item.EixoY], 
                    40
                )
                self.TELA.blit(
                    pygame.font.SysFont('Comic Sans MS', 40).render(
                        str(item.NumeroBola), 
                        False, 
                        (0, 0, 0)
                    ),
                    (item.EixoX - 10, item.EixoY - 25)
                )
            
            # Atualizar o soma de valores
            pygame.draw.circle(
                self.TELA, 
                CoresModel.BRANCO, 
                (self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas'] + 120, 280), 
                40
            )
            self.TELA.blit(
                font.render(
                    str(self.somaValores), 
                    False, 
                    (0, 0, 0)
                ),
                (self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas'] + 100, 250)
            )

        # Quando o resto da soma de valores for igual a 0, irá atualizar os valores e 
        if self.somaValores % 5 == 0:
            self.somaValores = 0
            
            pygame.draw.circle(
                self.TELA, 
                CoresModel.VERMELHO, 
                [orbe.EixoX, orbe.EixoY], 
                45
            )

            # Limpa a as orbes
            for item in self.listaOrbesClicados:
                pygame.draw.circle(
                    self.TELA, 
                    CoresModel.VERMELHO, 
                    [item.EixoX, item.EixoY], 
                    45
                )
                pygame.draw.circle(
                    self.TELA, 
                    CoresModel.VERMELHO, 
                    [item.EixoX, item.EixoY], 
                    40
                )
                self.TELA.blit(
                    pygame.font.SysFont('Comic Sans MS', 40).render(
                        str(item.NumeroBola), 
                        False, 
                        (0, 0, 0)
                    ),
                    (item.EixoX - 10, item.EixoY - 25)
                )

            # Gerar as orbes marcadas
            #self.gerarBolasVertical(
                #self.dicionarioTorres['primeiraTorreVertical']['eixoXBolas'], 
                #120, 
                #40
            #)
            
        else:
            # Adicionar as orbes selecionadas
            self.listaOrbesClicados.append(orbe)
            
            # Adicionar a borda no clique
            pygame.draw.circle(
                self.TELA, 
                CoresModel.VERDE, 
                [orbe.EixoX, orbe.EixoY], 
                45
            )
            pygame.draw.circle(
                self.TELA, 
                CoresModel.VERMELHO, 
                [orbe.EixoX, orbe.EixoY], 
                40
            )
            self.TELA.blit(
                pygame.font.SysFont('Comic Sans MS', 40).render(
                    str(orbe.NumeroBola), 
                    False, 
                    (0, 0, 0)
                ),
                (orbe.EixoX - 10, orbe.EixoY - 25)
            )

            # Atualizar o soma de valores
            pygame.draw.circle(
                self.TELA, 
                CoresModel.BRANCO, 
                (self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas'] + 120, 280), 
                40
            )
            self.TELA.blit(
                font.render(
                    str(self.somaValores), 
                    False, 
                    (0, 0, 0)
                ),
                (self.dicionarioTorres['terceiraTorreVerical']['eixoXBolas'] + 100, 250)
            )
