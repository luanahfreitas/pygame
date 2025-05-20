import pygame
from config import *
from init_screen import *
from game import *
from assets import *
from game_over import game_over_screen

#inicializa a tela
pygame.init()

#inicializa a musica
pygame.mixer.init()

#imagem de fundo
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("desFRUTANDO")

assets = load_assets()

pygame.mixer.music.load(assets['musica_normal'])
pygame.mixer.music.play(-1)

jogando = True 

while jogando:
    state = init_screen(screen,assets)
    #dificuldade do jogo
    if state in [EASY,MEDIUM,HARD]:
        pontos = tela_jogo(screen,state,assets)
        state = game_over_screen(screen, pontos, assets)

    else:
        jogando = False

pygame.quit()