import pygame, sys
from pygame.locals import *


class Tela:

    #Constante
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)

    X = 500
    Y = 500

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
                print(event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == 5:
                    self.desenhaJogo()
            pygame.display.update()

    #Função desenha elementos do Jogo
    def desenhaJogo(self):
        pygame.quit()
        sys.exit()
        print('teste')

    #Função desenha inicio do jogo
    def desenhaTelaInicial(self, TELA):

        #Texto Descritivo
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Multiplos de 5', True, self.BLUE)
        textRect = text.get_rect()
        textRect.center = (self.X // 2.5, self.Y // 4)
        TELA.blit(text, textRect)

        #Buttons
        pygame.draw.rect(TELA,self.BLUE,(self.X/3.5,self.Y/2.5,100,50))
        text = font.render('Jogar', True, self.GREEN)
        textRect = text.get_rect()
        textRect.center = (self.X/2.6,self.Y/2.2)
        TELA.blit(text, textRect)
