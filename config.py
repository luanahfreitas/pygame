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
MELANCIA_WIDTH = 80
MELANCIA_HEIGHT = 80

PESSEGO_WIDTH = 50
PESSEGO_HEIGHT = 50

MIRTILO_WIDTH = 30
MIRTILO_HEIGHT = 30

#faca
FACA_WIDTH = 20
FACA_HEIGHT = 40

#FONTE
FONT_TITLE = pygame.font.SysFont(None, 80)
FONT_BUTTON = pygame.font.SysFont(None, 40)


#IMAGENS
BASE_DIR = path.dirname(__file__)
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')


GAME = 1
QUIT = 0
EASY = 2
MEDIUM = 3
HARD = 4
OVER = 5