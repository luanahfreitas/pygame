import pygame
import assets
from config import *
from init_screen import *
from game import *
from assets import *

pygame.init()
pygame.mixer.init()



screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("desFRUTANDO")

jogando = True 

while jogando:
    state = init_screen(screen,load_assets)
    if state in [EASY,MEDIUM,HARD]:
        pontos = tela_jogo(screen,state,assets)
        #game over

    else:
        jogando = False

pygame.quit()