import pygame
from os import *

#CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


#TAMANHOS
#tela
WIDTH = 700
HEIGHT = 600

#frutas
MELANCIA_WIDTH = 110
MELANCIA_HEIGHT = 110

PESSEGO_WIDTH = 80
PESSEGO_HEIGHT = 80

MIRTILO_WIDTH = 50
MIRTILO_HEIGHT = 50

#faca
FACA_WIDTH = 40
FACA_HEIGHT = 80

#bomba
BOMBA_WIDTH = 60
BOMBA_HEIGHT = 60


#caminho dos arquivos
BASE_DIR = path.dirname(__file__)
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FONT_DIR = path.join(path.dirname(__file__), 'assets', 'font')


ON = 1
QUIT = 0
EASY = 2
MEDIUM = 3
HARD = 4
DONE = 5

FPS = 60