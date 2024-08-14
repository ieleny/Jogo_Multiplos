import pygame
from .Jogo import Jogo
from .CoresModel import CoresModel

class Menu:

    def __init__(self, TELA, X, Y):
        self.TELA = TELA
        self.X = X
        self.Y = Y

    #Função desenha inicio do jogo
    def desenhaTelaInicial(self):
        # Texto Descritivo
        fonte = pygame.font.Font('freesansbold.ttf', 40)
        text = fonte.render('Multiplos de 5', True, CoresModel.AZUL)
        textRect = text.get_rect()
        textRect.center = (self.X // 2, self.Y // 4)
        self.TELA.blit(text, textRect)

        # Botões
        fonte_botao = pygame.font.Font('freesansbold.ttf', 50)
        self.botao = pygame.draw.rect(
                                       self.TELA, 
                                       CoresModel.AZUL,
                                      (self.X // 3, self.Y // 2.5, 300, 70)
                                    )
        text = fonte_botao.render('Jogar', True, CoresModel.VERDE)
        textRect = text.get_rect()
        textRect.center = (self.X // 2.1, self.Y // 2.2)
        self.TELA.blit(text, textRect)

    # Função desenha elementos do Jogo
    def inicioJogo(self, event):
        # Verifica se a posição é do botão
        if self.botao.collidepoint(event.pos):
            jogo = Jogo(self.TELA, self.X, self.Y)
            self.TELA.fill(CoresModel.BRANCO)
            jogo.telaDoJogo()
