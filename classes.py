import pygame
import random
from assets import *
from config import *

# Definindo Faca, Frutas e Bomba 

class Fruta(pygame.sprite.Sprite):
    def __init__(self, imagem_fruta, tipo='normal', velocidade=3, direcao='baixo'):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_fruta  #imagem varia de acordo com a dificuldade selecionada
        self.tipo = tipo  #'normal', 'dourada', 'congelada'
        self.speed = velocidade  #velocidade que a fruta cai
        self.direction = direcao  #direção que a fruta cai
        self.rect = self.image.get_rect()
        self.cortada = False  #verifica se a fruta foi cortada ou não

        #inicializando a posição da fruta de acordo com a direção
        if direcao == 'baixo':
            self.rect.midtop = (random.randint(30, WIDTH - 30), -50)
        elif direcao == 'esquerda':
            self.rect.midleft = (-50, random.randint(50, HEIGHT - 50))
        elif direcao == 'direita':
            self.rect.midright = (WIDTH + 50, random.randint(50, HEIGHT - 50))  
            
    def update(self):
        #velocidades em cada direção
        if self.direction == 'baixo':
            self.rect.y += self.speed
        elif self.direction == 'esquerda':
            self.rect.x += self.speed
        elif self.direction == 'direita':
            self.rect.x -= self.speed


class Bomba(pygame.sprite.Sprite):
    def __init__(self, assets, velocidade=3, direcao='baixo'):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['bomba']  #imagem da bomba
        self.speed = velocidade  #velocidade que a bomba cai
        self.direction = direcao  #direção que a bomba cai
        self.rect = self.image.get_rect()

        #inicializando a posição da bomba de acordo com a direção
        if direcao == 'baixo':
            self.rect.midtop = (random.randint(30, WIDTH - 30), -50)
        elif direcao == 'esquerda':
            self.rect.midleft = (-50, random.randint(50, HEIGHT - 50))
        elif direcao == 'direita':
            self.rect.midright = (-50, random.randint(50, HEIGHT - 50))  

    def update(self):
        #velocidades em cada direção
        if self.direction == 'baixo':
            self.rect.y += self.speed
        elif self.direction == 'esquerda':
            self.rect.x += self.speed
        elif self.direction == 'direita':
            self.rect.x -= self.speed


class Particula(pygame.sprite.Sprite):
    def __init__(self, x, y, cor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 4)) #tamanho da partícula
        self.image.fill(cor) #cor da partícula
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = random.randint(-5, 5)  #velocidade horizontal aleatória
        self.speed_y = random.randint(-5, -1)  #velocidade vertical aleatória (só para cima)
        self.life = 20  #quanto tempo ela dura

    def update(self):
        #atualiza a posição da partícula
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.life -= 1
        if self.life <= 0:
            self.kill()  #quando acabar a vida, a partícula é removida
