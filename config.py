import pygame
from os import *

#CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


#TAMANHOS
#tela
WIDTH = 450
HEIGHT = 600
FPS = 60

#frutas
MELANCIA_WIDTH = 0
MELANCIA_HEIGHT = 0

PESSEGO_WIDTH = 0
PESSOGO_HEIGHT = 0

MIRTILO_WIDTH = 0
MIRTILO_HEIGHT = 0

#faca
FACA_WIDTH = 0
FACA_HEIGHT = 0

#FONTE
FONT_TITLE = pygame.font.SysFont(None, 80)
FONT_BUTTON = pygame.font.SysFont(None, 40)


#IMAGENS
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')


GAME = 1
QUIT = 0
EASY = 2
MEDIUM = 3
HARD = 4
OVER = 5