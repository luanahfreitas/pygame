import pygame
import random
from assets import *
from config import *

# Definindo Faca, Frutas e Bomba 

class Fruta(pygame.sprite.Sprite):
    def __init__(self, imagem_fruta, tipo='normal', velocidade=3, direction='baixo'):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_fruta  #imagem varia de acordo com a dificuldade selecionada
        self.tipo = tipo  #'normal', 'dourada', 'congelada'
        self.speed = velocidade  #velocidade que a fruta cai
        self.direction = direction  #direção que a fruta cai
        self.rect = self.image.get_rect()

        if direction == 'baixo':
            self.rect.midtop = (random.randint(30, WIDTH - 30), -50)
        elif direction == 'esquerda':
            self.rect.midleft = (-50, random.randint(50, HEIGHT - 50))
        elif direction == 'direita':
            self.rect.midright = (-50, random.randint(50, HEIGHT - 50))  
            
        self.particle.timer = 0

    def update(self):
        if self.direcao == 'baixo':
            self.rect.y += self.speed
        elif self.direcao == 'esquerda':
            self.rect.x += self.speed
        elif self.direcao == 'direita':
            self.rect.x -= self.speed

        # Frutas explosivas geram partículas enquanto caem
        if self.tipo == 'explosiva':
            now = pygame.time.get_ticks()
            if now - self.particle_timer > 100:
                self.particle_timer = now
                for _ in range(3):
                    cor = (255, 100, 0)
                    self.groups()[0].add(Particula(self.rect.centerx, self.rect.centery, cor))


class Bomba(pygame.sprite.Sprite):
    def __init__(self, assets, velocidade=3, direction='baixo'):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['bomba']
        self.speed = velocidade
        self.direction = direction  #direção que a bomba cai
        self.rect = self.image.get_rect()

        if direction == 'baixo':
            self.rect.midtop = (random.randint(30, WIDTH - 30), -50)
        elif direction == 'esquerda':
            self.rect.midleft = (-50, random.randint(50, HEIGHT - 50))
        elif direction == 'direita':
            self.rect.midright = (-50, random.randint(50, HEIGHT - 50))  
            
        self.particle.timer = 0

    def update(self):
        if self.direcao == 'baixo':
            self.rect.y += self.speed
        elif self.direcao == 'esquerda':
            self.rect.x += self.speed
        elif self.direcao == 'direita':
            self.rect.x -= self.speed


class Particula(pygame.sprite.Sprite):
    def __init__(self, x, y, cor):
        pygame.sprite.Sprite.__init__(self)
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

class Explosão(pygame.sprite.Sprite):
    def __init__(self, center, animacao):
        pygame.sprite.Sprite.__init__(self)
        self.animacao = animacao
        self.image = self.animacao[self.frame]
        self.rect = self.image.get_rect(center=(center))
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_duration = 50  # Duração de cada frame em milissegundos

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(self.image):
                self.kill()