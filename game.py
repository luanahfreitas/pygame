import pygame
from assets import load_assets
from config import *
import random
from classes import Faca, Frutas, Bomba, Particula


def tela_jogo(screen,dificuldade,assets):
    clock = pygame.time.Clock()
    tempo_inicio = pygame.time.get_ticks()

    vidas = 3
    vida_estado = [True,True,True]

    fonte = assets['padrao_font']

    facas = pygame.sprite.Group()
    bombas = pygame.sprite.Group()
    frutas = pygame.sprite.Group()
    particulas = pygame.sprite.Group()

    faca_atual = Faca(WIDTH // 2, HEIGHT - 10, assets)
    facas.add(faca_atual)

    if dificuldade == EASY:
        imagem_fruta = assets['melancia']
        imagem_fundo = assets['fundo melancia']
    elif dificuldade == MEDIUM:
        imagem_fruta = assets['pessego']
        imagem_fundo = assets['fundo pessego']
    elif dificuldade == HARD:
        imagem_fruta = assets['mirtilo']
        imagem_fundo = assets['fundo mirtilo']

    pontos = 0
    state = ON

    pygame.mixer.music.load(assets['musica_normal'])
    pygame.mixer.music.play(-1)  # loop infinito da musica
    pygame.mixer.music.set_volume(0.3)

    modo_bonus = False
    bonus_timer = 0
    FPS_padrao = 60

    while state != DONE:
        clock.tick(FPS_padrao)
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
        
        r = random.randint(1, 100)
        if r <= 5:
            frutas.add(Frutas(assets['fruta_dourada'], tipo='dourada'))
        elif r <= 10:
            frutas.add(Frutas(assets['fruta_congelada'], tipo='congelada'))
        elif r <= 50:
            frutas.add(Frutas(imagem_fruta, tipo='normal'))

        if tempo_passado > 15 and random.randint(1,80) == 1:
            bombas.add(Bomba(assets))


        frutas.update()
        bombas.update()
        particulas.update()

        for fruta in frutas:
            if fruta.rect.top > HEIGHT:
                fruta.kill()
                vidas -= 1
                if vidas >= 0:
                    animacao_coracao(screen,assets,vidas)
                    vida_estado[vidas] = False
                if vidas <= 0:
                    pygame.mixer.music.stop()
                    fade_out(screen)
                    explodir_tela(screen, assets)
                    return pontos

        #colisões - faca com a fruta
        colisoes = pygame.sprite.groupcollide(facas, frutas, True, True)
        for faca, frutas in colisoes.items():
            for fruta in frutas:
                if fruta.tipo == 'dourada':
                    for _ in range(20):
                        particulas.add(Particula(fruta.rect.centerx, fruta.rect.centery, (255, 215, 0)))  # dourado
                    pontos += 20
                    modo_bonus = True
                    bonus_timer = pygame.time.get_ticks()  #inicia o contagem do modo bônus
                    #pygame.mixer.music.load(assets['bonus_musica'])
                    #pygame.mixer.music.play(-1)  # loop infinito da musica

                elif fruta.tipo == 'congelada':
                    for _ in range(20):
                        particulas.add(Particula(fruta.rect.centerx, fruta.rect.centery, (150, 200, 255)))  # azul claro
                    FPS_padrao = max(20, FPS_padrao - 10)
                    congelar_tela(screen)
                    pontos +=5 * (2 if modo_bonus else 1)

                else:  #normal
                    for _ in range(15):
                        particulas.add(Particula(fruta.rect.centerx, fruta.rect.centery, (255, 255, 0)))
                    pontos += 5 * (2 if modo_bonus else 1)

                assets['faca_sound'].play()  #som da faca cortando a fruta

        #colisões - faca com a bomba
        if pygame.sprite.groupcollide(facas,bombas,True,False):
            assets['explosion_sound'].play()
            pygame.mixer.music.stop()
            shake_screen(screen)
            fade_out(screen)
            explodir_tela(screen,assets)
            return pontos
        
        screen.blit(imagem_fundo, (0,0))

        if modo_bonus:
            tempo = (pygame.time.get_ticks() - bonus_timer) / 1000
            if tempo > 15:
                modo_bonus = False
                FPS_padrao = 60
                pygame.mixer.music.load(assets['musica_normal'])
                pygame.mixer.music.play(-1)

        #desenha os sprites na tela
        frutas.draw(screen)
        particulas.draw(screen)
        bombas.draw(screen)
        facas.draw(screen)

        #coloca os pontos na tela de jogo 
        texto = fonte.render(f"Pontos: {pontos}", True, WHITE)  #cor branca
        screen.blit(texto, (10, 10))  #tamanho do texto

        #desenha as vidas na tela - corações
        for i in range(3):
            x = 10 + i * 35
            y = 50
            if vida_estado[i]:
                screen.blit(assets['vida cheia'], (x, y))
            else:
                screen.blit(assets['vida vazia'], (x, y))
        
        pygame.display.flip()
        

def explodir_tela(screen,assets):
    animacao = assets['explosion_anim']
    x = (WIDTH - 32) // 2
    y = (HEIGHT - 32) // 2

    for frame in animacao:
        screen.fill(BLACK)
        screen.blit(frame,(x,y))
        pygame.display.flip()


#fade out efeito
def fade_out(screen, velocidade=10):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0, 0, 0))

    for alpha in range(0, 255, velocidade):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)


#Shake effect (ajuda de inteligencia artificial)
def shake_screen(screen, intensidade = 5, duracao = 10):
    fundo_original = screen.copy()
    for _ in range(duracao):
        offset_x = random.randint(-intensidade, intensidade)
        offset_y = random.randint(-intensidade, intensidade)
        screen.blit(fundo_original, (offset_x, offset_y))
        pygame.display.flip()
        pygame.time.delay(30)


#Animação de corações
def animacao_coracao(screen,assets,i,duracao=10):
    cheio = assets['vida cheia']
    vazio = assets['vida vazia']
    x = 10 + i * 35
    y = 50
    for alpha in range(255, 0, -int(255 / duracao)):
        # Cria uma cópia da imagem com opacidade reduzido
        img = cheio.copy()
        img.set_alpha(alpha)

        screen.blit(vazio, (x, y))    
        screen.blit(img, (x, y))
        pygame.display.flip()
        pygame.time.delay(30)

def congelar_tela(screen, duracao=5000):
    congelado = pygame.Surface((WIDTH, HEIGHT))
    congelado.fill((100, 180, 255))  # azul claro
    congelado.set_alpha(100)         # Transparente
    screen.blit(congelado, (0, 0))
    pygame.display.flip()
    pygame.time.delay(duracao)

