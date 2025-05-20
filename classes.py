import pygame
import random
from assets import *
from config import *

# Definindo Faca, Frutas e Bomba 

class Faca(pygame.sprite.Sprite):
    def __init__(self, x, y, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['faca']
        #inicializa a faca na posição do meio da tela
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed_y = 0  #nao meche no eixo y
        self.speed_x = 7  #velocidade da faca
        self.lancada = False  

    def update(self, teclas):
        if not self.lancada:
            #anda para os lados
            if teclas[pygame.K_a]:
                self.rect.x -= self.speed_x
            if teclas[pygame.K_d]:
                self.rect.x += self.speed_x

            #determina os limites da tela
            if self.rect.left < 0:
                self.rect.left = 0 
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH 
            
        else:
            self.rect.y += self.speed_y
            if self.rect.bottom < 0:
                self.kill() #remove a faca se ela sair da tela

    #lanca a faca
    def lancar(self):
        if not self.lancada:
            self.lancada = True
            self.speed_y = -10  # velocidade de lançamento (negativa porque vai para cima)
    

class Frutas(pygame.sprite.Sprite):
    def __init__(self, imagem_fruta, tipo='normal'):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_fruta  #imagem varia de acordo com a dificuldade selecionada
        self.tipo = tipo  #'normal', 'dourada', 'congelada'
        self.rect = self.image.get_rect(midtop=(random.randint(30, WIDTH - 40), -50))  #frutas aparecem em posições aleatórias
        self.speed = 3  #velocidade que a fruta cai
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()
    

class Bomba(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['bomba']
        self.rect = self.image.get_rect(midtop=(random.randint(30, WIDTH - 40), -50))
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


class Particula(pygame.sprite.Sprite):
    def __init__(self, x, y, cor):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(cor)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, -1)
        self.life = 20  #quanto tempo ela dura

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.life -= 1
        if self.life <= 0:
            self.kill()