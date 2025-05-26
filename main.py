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

#cria a tela
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("desFRUTANDO")

assets = load_assets()

pygame.mixer.music.load(assets['musica_normal'])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

jogando = True 

while jogando:
    state = init_screen(screen,assets)
    #dificuldade do jogo
    if state in [EASY,MEDIUM,HARD]:
        pontos = tela_jogo(screen,state,assets)  #jogo e retorna os pontos

        state = game_over_screen(screen, pontos, assets)  #tela game over

    else:
        jogando = False

pygame.quit()