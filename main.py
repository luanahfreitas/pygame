import pygame
import assets
from config import *
from init_screen import *
from game import *
from assets import *
from game_over import game_over_screen

pygame.init()
pygame.mixer.init()



screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("desFRUTANDO")

#musica de fundo
pygame.mixer.music.load('assets/snd/musica.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)  #loop infinito da música

jogando = True 

while jogando:
    state = init_screen(screen,load_assets)
    if state in [EASY,MEDIUM,HARD]:
        pontos = tela_jogo(screen,state,assets)
        state = game_over_screen(screen, pontos, load_assets())

    else:
        jogando = False

pygame.quit()