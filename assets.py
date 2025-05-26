import pygame
import os
from config import *


def load_assets():
    assets = {}

    #imagens(frutas, faca, bomba, fundos)
    #fundos 
    assets['background'] = pygame.image.load(os.path.join(IMG_DIR, 'fundo.jpg')).convert()

    #modo normal
    assets['facil'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez vermelho.jpg')).convert()
    assets['medio'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez laranja.png')).convert()
    assets['dificil'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez azul.jpg')).convert()

    #modo extremo
    assets['facil'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez vermelho copy.jpg')).convert()
    assets['medio'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez laranja copy.png')).convert()
    assets['dificil'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez azul copy.jpg')).convert()

    #frutas
    melancia = pygame.image.load(os.path.join(IMG_DIR, 'melancia.png')).convert_alpha()
    assets['melancia'] = pygame.transform.scale(melancia, (MELANCIA_WIDTH, MELANCIA_HEIGHT))

    mirtilo = pygame.image.load(os.path.join(IMG_DIR, 'mirtilo.webp')).convert_alpha()
    assets['mirtilo'] = pygame.transform.scale(mirtilo, (MIRTILO_WIDTH, MIRTILO_HEIGHT))

    pessego = pygame.image.load(os.path.join(IMG_DIR, 'pessego.png')).convert_alpha()
    assets['pessego'] = pygame.transform.scale(pessego, (PESSEGO_WIDTH, PESSEGO_HEIGHT))

    #faca
    faca = pygame.image.load(os.path.join(IMG_DIR, 'faca.png')).convert_alpha()
    assets['faca'] = pygame.transform.scale(faca, (FACA_WIDTH, FACA_HEIGHT))
    
    #bomba
    bomba = pygame.image.load(os.path.join(IMG_DIR, 'bomba.webp')).convert_alpha()
    assets['bomba'] = pygame.transform.scale(bomba, (BOMBA_WIDTH, BOMBA_HEIGHT))

    #vida - coracoes
    cheio = pygame.image.load(os.path.join(IMG_DIR, 'vida cheia.png')).convert_alpha()
    assets['vida cheia'] = pygame.transform.scale(cheio, (30, 30))
    
    vazio = pygame.image.load(os.path.join(IMG_DIR, 'vida vazia.png')).convert_alpha()
    assets['vida vazia'] = pygame.transform.scale(vazio, (30, 30))


    #frutas especiais
    dourada = pygame.image.load(os.path.join(IMG_DIR, 'dourada.png')).convert_alpha()
    assets['dourada'] = pygame.transform.scale(dourada, (50, 50))
    
    gelo = pygame.image.load(os.path.join(IMG_DIR, 'gelo.webp')).convert_alpha()
    assets['gelo'] = pygame.transform.scale(gelo, (50, 50))

    abacaxi = pygame.image.load(os.path.join(IMG_DIR, 'abacaxi.png')).convert_alpha()
    assets['explosiva'] = pygame.transform.scale(abacaxi, (50, 50))


    #fonts
    assets['titulo_font'] = pygame.font.Font(os.path.join(FONT_DIR, 'titulo.ttf'), 80)
    assets['gameover_font'] = pygame.font.Font(os.path.join(FONT_DIR, 'gameover.ttf'), 80)
    assets['padrao_font'] = pygame.font.Font(os.path.join(FONT_DIR, 'padrao.ttf'), 40)
    

    #sons
    assets['explosion_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'bomb.wav'))
    assets['faca_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'faca.wav'))
    assets['musica_normal'] = os.path.join(SND_DIR, 'musica.mp3')
    assets['freeze_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'freeze.mp3'))
    assets['bonus_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som dourado.wav'))
    assets['vida'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'vida ganha.wav'))
    #assets['brilho'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'brilho.wav'))

    #animacao
    explosao_fruta = []
    for i in range(4,1):
        filename = f'magic_0{i}.png'
        path_img = os.path.join(IMG_DIR, filename)
        img = pygame.image.load(path_img).convert_alpha()
        img = pygame.transform.scale(img, (32, 32))
        explosao_fruta.append(img)

    assets['explosao_fruta'] = explosao_fruta

    return assets
