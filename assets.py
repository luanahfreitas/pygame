import pygame
import os
from config import *


def load_assets():
    assets = {}

    #imagens(frutas, faca, bomba, fundos)
    assets['background'] = pygame.image.load(os.path.join(IMG_DIR, 'fundo.jpeg')).convert()

    assets['fundo melancia'] = pygame.image.load(os.path.join(IMG_DIR, 'fundo melancia.webp')).convert()
    assets['fundo pessego'] = pygame.image.load(os.path.join(IMG_DIR, 'fundo pessego.jpg')).convert()
    assets['fundo mirtilo'] = pygame.image.load(os.path.join(IMG_DIR, 'fundo mirtilo.jpg')).convert()

    melancia = pygame.image.load(os.path.join(IMG_DIR, 'melancia.png')).convert()
    assets['melancia'] = pygame.transform.scale(melancia, (MELANCIA_WIDTH, MELANCIA_HEIGHT))

    mirtilo = pygame.image.load(os.path.join(IMG_DIR, 'mirtilo.webp')).convert()
    assets['mirtilo'] = pygame.transform.scale(mirtilo, (MIRTILO_WIDTH, MIRTILO_HEIGHT))

    pessego = pygame.image.load(os.path.join(IMG_DIR, 'pessego.png')).convert()
    assets['pessego'] = pygame.transform.scale(pessego, (PESSEGO_WIDTH, PESSEGO_HEIGHT))

    faca = pygame.image.load(os.path.join(IMG_DIR, 'faca.png')).convert()
    assets['faca'] = pygame.transform.scale(faca, (FACA_WIDTH, FACA_HEIGHT))
    
    bomba = pygame.image.load(os.path.join(IMG_DIR, 'bomba.webp')).convert()
    assets['bomba'] = pygame.transform.scale(bomba, (BOMBA_WIDTH, BOMBA_HEIGHT))

    cheio = pygame.image.load(os.path.join(IMG_DIR, 'vida cheia.png')).convert()
    assets['vida cheia'] = pygame.transform.scale(cheio, (30, 30))
    
    vazio = pygame.image.load(os.path.join(IMG_DIR, 'vida vazia.png')).convert()
    assets['vida vazia'] = pygame.transform.scale(vazio, (30, 30))

    #frutas especiais
    #adicionar frutas douradas
    #adicionar frutas congeladas

    #fonts
    assets['titulo_font'] = pygame.font.Font(os.path.join(FONT_DIR, 'titulo.ttf'), 80)
    assets['gameover_font'] = pygame.font.Font(os.path.join(FONT_DIR, 'gameover.ttf'), 80)
    assets['padrao_font'] = pygame.font.Font(os.path.join(FONT_DIR, 'padrao.ttf'), 40)
    

    #sons
    assets['explosion_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'bomb.wav'))
    assets['faca_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'faca.wav'))
    assets['musica'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'musica.mp3'))
    #adicionar bonus musica
    #adicionar pew
    #adicionar som de perder vida

    return assets
