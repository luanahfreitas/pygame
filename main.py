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
screen = pygame.display.set_mode((WIDTH,HEIGHT))  #tamanho da tela
pygame.display.set_caption("desFRUTANDO")  #titulo da tela

assets = load_assets()

pygame.mixer.music.load(assets['musica_normal'])  #carrega a musica de fundo
pygame.mixer.music.play(-1)  #toca a musica em loop
pygame.mixer.music.set_volume(0.5)  #volume da musica

jogando = True 

while jogando:
    state = init_screen(screen,assets)  #carrega o estado do jogo de acordo com o botão clicado
    #dificuldade do jogo
    if state in [EASY,MEDIUM,HARD]:
        pontos = tela_jogo(screen,state,assets)  #jogo e retorna os pontos

        state = game_over_screen(screen, pontos, assets)  #tela game over

    else:
        jogando = False

pygame.quit()