import pygame, sys
from pygame.locals import *
from .Jogo import Jogo


class Tela:

    #Constante
    BRANCO = (255, 255, 255)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 128)
    PRETO = (0, 0, 0, 0)
    CINZA = (128, 128, 128)

    X = 1000
    Y = 600

    TELA = pygame.display.set_mode((X, Y))

    #Construtor
    def __init__(self):
        self.telaJogo()

    #Função do game Loop da tela
    def telaJogo(self):

        pygame.init()

        self.TELA.fill(self.CINZA)
        pygame.display.set_caption('Multiplos de 5')

        self.desenhaTelaInicial()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    self.inicioJogo(event)
            pygame.display.update()

    #Função desenha elementos do Jogo
    def inicioJogo(self, event):
        
        #Verificar se a posição é do botão
        if self.botao.collidepoint(event.pos):
            jogo = Jogo(self.TELA, self.X, self.Y)
            self.TELA.fill(self.BRANCO)
            jogo.telaDoJogo()

    #Função desenha inicio do jogo
    def desenhaTelaInicial(self):

        #Texto Descritivo
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render('Multiplos de 5', True, self.AZUL)
        textRect = text.get_rect()
        textRect.center = (self.X // 2, self.Y // 4)
        self.TELA.blit(text, textRect)

        #Buttons
        font_button = pygame.font.Font('freesansbold.ttf', 50)
        self.botao = pygame.draw.rect(self.TELA, self.AZUL,
                                      (self.X // 3, self.Y // 2.5, 300, 70))
        text = font_button.render('Jogar', True, self.VERDE)
        textRect = text.get_rect()
        textRect.center = (self.X // 2.1, self.Y // 2.2)
        self.TELA.blit(text, textRect)
