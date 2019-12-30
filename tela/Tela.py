import pygame, sys
from pygame.locals import *


class Tela:

    #Constante
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)

    X = 400
    Y = 300

    #Construtor
    def __init__(self):
        self.telaJogo()

    #Função do game Loop da tela
    def telaJogo(self):

        pygame.init()

        TELA = pygame.display.set_mode((self.X, self.Y))
        TELA.fill(self.WHITE)
        pygame.display.set_caption('Multiplos 5')

        while True:

            self.desenhaTelaInicial(TELA)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    #Função desenha elementos do Jogo
    def desenhaJogo(self):
        print('teste')

    #Função desenha inicio do jogo
    def desenhaTelaInicial(self, TELA):

        #Texto Descritivo
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Multiplos de 5', True, self.BLUE)
        textRect = text.get_rect()
        textRect.center = (self.X // 2, self.Y // 4)
        TELA.blit(text, textRect)

        #Buttons
