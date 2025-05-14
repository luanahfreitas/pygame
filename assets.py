import pygame
import os
from config import *


def load_assets():
    assets = {}

    #imagens
    assets['background'] = pygame.image.load(os.path.join(IMG_DIR, 'tela_init.jpg')).convert()

    melancia = pygame.image.load(os.path.join(IMG_DIR, 'melancia.png')).convert()
    assets['melancia'] = pygame.transform.scale(melancia, (MELANCIA_WIDTH, MELANCIA_HEIGHT))


    mirtilo = pygame.image.load(os.path.join(IMG_DIR, 'mirtilo.png')).convert()
    assets['mirtilo'] = pygame.transform.scale(mirtilo, (MIRTILO_WIDTH, MIRTILO_HEIGHT))

    pessego = pygame.image.load(os.path.join(IMG_DIR, 'pessego.png')).convert()
    assets['pessego'] = pygame.transform.scale(pessego, (PESSEGO_WIDTH, PESSEGO_HEIGHT))

    faca = pygame.image.load(os.path.join(IMG_DIR, 'faca.png')).convert()
    assets['faca'] = pygame.transform.scale(faca, (FACA_WIDTH, FACA_HEIGHT))

    #PEGAR IMAGEM DE BOMBA

    
    #animações(explosão)
    explosion_anim = []
    for i in range(9):
        filename = f'regularExplosion0{i}.png'
        path = os.path.join(IMG_DIR, filename)
        img = pygame.image.load(path).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets['explosion_anim'] = explosion_anim


    #fonts
    assets['score_font'] = pygame.font.SysFont('Arial', 28)


    #sons
    assets['explosion_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'bomb.wav'))
    assets['faca_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'faca.wav'))

    #pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    #pygame.mixer.music.set_volume(0.4)

    return assets
