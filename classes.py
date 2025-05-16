import pygame
import random
from assets import *
from config import *

class Faca(pygame.sprite.Sprite):
    def __init__(self, x, y, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['faca']
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed_y = 0  
        self.speed_x = 7  
        self.lancada = False  

    def update(self, teclas):
        if not self.lancada:
            if teclas[pygame.K_a]:
                self.rect.x -= self.speed_x
            if teclas[pygame.K_d]:
                self.rect.x += self.speed_x

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            
        else:
            self.rect.y += self.speed_y
            if self.rect.bottom < 0:
                self.kill()


    def lancar(self):
        if not self.lancada:
            self.lancada = True
            self.speed_y = -10
    

class Frutas(pygame.sprite.Sprite):
    def __init__(self, imagem_fruta):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_fruta
        self.rect = self.image.get_rect(midtop=(random.randint(30, WIDTH - 40), -50))
        self.speed = 3
    
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