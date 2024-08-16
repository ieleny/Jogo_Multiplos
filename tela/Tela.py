import pygame, sys
from pygame.locals import *
from .Menu import Menu
from .CoresModel import CoresModel
from .TamanhoTela import TamanhoTela

class Tela:
    TELA = pygame.display.set_mode((TamanhoTela.LARGURA_TELA, TamanhoTela.ALTURA_TELA))

    # Construtor
    def __init__(self):
        self.telaJogo()

    # Função do game Loop da tela
    def telaJogo(self):
        # Salvar se o usuário clicou no botão do inicio do jogo
        clicouBotaoInicioJogo = False
        
        # Inicializar o jogo
        pygame.init()

        menu = Menu(self.TELA)
        
        # Adicionar cor na tela
        self.TELA.fill(CoresModel.CINZA)
        pygame.display.set_caption('Multiplos de 5')

        menu.desenhaTelaInicial()

        # Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and clicouBotaoInicioJogo == False:
                    menu.inicioJogo(event)
                    clicouBotaoInicioJogo = True
            pygame.display.update()
        