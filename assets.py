import pygame
import os
from config import *


def load_assets():
    assets = {}

    #imagens(frutas, faca, bomba, fundos)
    #fundos 
    assets['background'] = pygame.image.load(os.path.join(IMG_DIR, 'fundo.jpeg')).convert()
    #modo normal
    assets['facil'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez vermelho.jpg')).convert()
    assets['medio'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez laranja.png')).convert()
    assets['dificil'] = pygame.image.load(os.path.join(IMG_DIR, 'xadrez azul.jpg')).convert()

    #modo extremo
    assets['facil_extremo'] = pygame.image.load(os.path.join(IMG_DIR, 'melancia extremo.webp')).convert()
    assets['medio_extremo'] = pygame.image.load(os.path.join(IMG_DIR, 'pessego extremo.png')).convert()
    assets['dificil_extremo'] = pygame.image.load(os.path.join(IMG_DIR, 'mirtilo extremo.jpg')).convert()

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
    #adicionar som de ganhar vida
    #barulho de brilho 
    

    return assets
