import pygame
from assets import load_assets
from config import *
import random
from classes import Faca, Frutas, Bomba

print("Faca está definida como:", Faca)

def tela_jogo(screen,dificuldade,assets):
    clock = pygame.time.Clock()
    tempo_inicio = pygame.time.get_ticks()
    
    fonte = assets['padrao_font']

    facas = pygame.sprite.Group()
    bombas = pygame.sprite.Group()
    frutas = pygame.sprite.Group()

    faca_atual = Faca(WIDTH // 2, HEIGHT - 10, assets)
    facas.add(faca_atual)

    if dificuldade == EASY:
        imagem_fruta = [assets['melancia']]
        imagem_fundo = assets['fundo melancia']
    elif dificuldade == MEDIUM:
        imagem_fruta = [assets['pessego']]
        imagem_fundo = assets['fundo pessego']
    elif dificuldade == HARD:
        imagem_fruta = [assets['mirtilo']]
        imagem_fundo = assets['fundo mirtilo']

    pontos = 0
    state = ON

    while state != DONE:
        clock.tick(FPS)
        tempo_passado = (pygame.time.get_ticks() - tempo_inicio) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pontos
    
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not faca_atual.lancada:
                    faca_atual.lancar()
                    #assets['pew'].play()
                
        teclas = pygame.key.get_pressed()

        for faca in facas:
            if not faca.lancada:
                faca.update(teclas)
            else:
                faca.update(None)

        if len(facas) == 0:
            faca_atual = Faca(WIDTH // 2, HEIGHT - 10, assets)
            facas.add(faca_atual)

        
        if random.randint(1,50) == 1:
            frutas.add(Frutas(imagem_fruta[0]))

        if tempo_passado > 15 and random.randint(1,80) == 1:
            bombas.add(Bomba(assets))


        frutas.update()
        bombas.update()

        #colisões
        if pygame.sprite.groupcollide(facas,frutas,True,True):
            pontos += 5
            assets['faca_sound'].play()

        if pygame.sprite.groupcollide(facas,bombas,True,False):
            assets['explosion_sound'].play()
            explodir_tela(screen,assets)
            return pontos
        
        screen.fill(imagem_fundo, (0,0))
        frutas.draw(screen)
        bombas.draw(screen)
        facas.draw(screen)

        texto = fonte.render(f"Pontos: {pontos}", True, WHITE)
        screen.blit(texto, (10, 10))
        pygame.display.flip()

def explodir_tela(screen,assets):
    animacao = assets['explosion_anim']
    x = (WIDTH - 32) // 2
    y = (HEIGHT - 32) // 2

    for frame in animacao:
        screen.fill(BLACK)
        screen.blit(frame,(x,y))
        pygame.display.flip()
