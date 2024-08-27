import pygame
from .Jogo import Jogo
from .CoresModel import CoresModel
from .TamanhoTela import TamanhoTela

class Menu:

    def __init__(self, TELA):
        self.TELA = TELA

    #Função desenha inicio do jogo
    def desenhaTelaInicial(self):
        # Texto Descritivo
        fonte = pygame.font.Font('freesansbold.ttf', 40)
        text = fonte.render('Multiplos de 5', True, CoresModel.AZUL)
        textRect = text.get_rect()
        textRect.center = (TamanhoTela.LARGURA_TELA // 2, TamanhoTela.ALTURA_TELA // 4)
        self.TELA.blit(text, textRect)

        # Botões
        fonte_botao = pygame.font.Font('freesansbold.ttf', 50)
        self.botao = pygame.draw.rect(
                                       self.TELA, 
                                       CoresModel.AZUL,
                                      (TamanhoTela.LARGURA_TELA // 3, TamanhoTela.ALTURA_TELA // 2.5, 300, 70)
                                    )
        text = fonte_botao.render('Jogar', True, CoresModel.VERDE)
        textRect = text.get_rect()
        textRect.center = (TamanhoTela.LARGURA_TELA // 2.1, TamanhoTela.ALTURA_TELA // 2.2)
        self.TELA.blit(text, textRect)

    # Função desenha elementos do Jogo
    def inicioJogo(self, event, jogo):
        # Verifica se a posição é do botão
        if self.botao.collidepoint(event.pos):
            self.TELA.fill(CoresModel.BRANCO)
            jogo.telaDoJogo()