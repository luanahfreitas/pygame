import pygame
from assets import load_assets
from config import *
import random
from classes import Fruta, Bomba, Particula, Explosão


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
    explosoes = pygame.sprite.Group()

    if dificuldade == EASY:
        imagem_fruta = assets['melancia']
        imagem_fundo = assets['facil']
        fundo_extremo = assets['facil_extremo']
    elif dificuldade == MEDIUM:
        imagem_fruta = assets['pessego']
        imagem_fundo = assets['medio']
        fundo_extremo = assets['medio_extremo']
    elif dificuldade == HARD:
        imagem_fruta = assets['mirtilo']
        imagem_fundo = assets['dificil']
        fundo_extremo = assets['dificil_extremo']

    fundo_atual = imagem_fundo

    pontos = 0
    state = ON

    pygame.mixer.music.load(assets['musica_normal'])
    pygame.mixer.music.play(-1)  # loop infinito da musica
    pygame.mixer.music.set_volume(0.3)

    congelado = False
    congelado_timer = 0
    duracao_congelado = 5000
    
    modo_bonus = False
    bonus_timer = 0
    FPS_padrao = 60

    #controladores de tempo
    tempo_ultima_fruta = pygame.time.get_ticks()
    intervalo_fruta = 1200  # 1 fruta a cada 1.2 segundos

    tempo_ultima_bomba = pygame.time.get_ticks()
    intervalo_bomba = 4000  # bomba só pode cair a cada 4 segundos

    

    while state != DONE:
        clock.tick(FPS_padrao)
        tempo_atual = pygame.time.get_ticks()
        tempo_passado = (tempo_atual - tempo_inicio) / 1000

        direcoes = ['baixo']
        velocidade_padrao = 3 + pontos // 30
        if pontos >= 150:
            direcoes = ['baixo', 'esquerda', 'direita']
            fundo_atual = fundo_extremo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pontos
                
        

        #frutas com intervalo de tempo
        if tempo_atual - tempo_ultima_fruta > intervalo_fruta:
            r = random.randint(1, 100)
            if pontos >= 20:
                if r <= 5:
                    frutas.add(Fruta(assets['dourada'], tipo='dourada', velocidade=velocidade_padrao, direcao=random.choice(direcoes)))
                elif r <= 10:
                    frutas.add(Fruta(assets['gelo'], tipo='congelada', velocidade=velocidade_padrao, direcao=random.choice(direcoes)))
                elif r <= 80:
                    frutas.add(Fruta(assets['explosiva'], tipo='explosiva', velocidade=velocidade_padrao, direcao=random.choice(direcoes)))
                else:
                    frutas.add(Fruta(imagem_fruta, tipo='normal', velocidade=velocidade_padrao, direcao=random.choice(direcoes)))

            else:
                frutas.add(Fruta(imagem_fruta, tipo='normal', velocidade=velocidade_padrao, direcao=random.choice(direcoes)))
            tempo_ultima_fruta = tempo_atual



        #bombas - só depois de 15s
        if tempo_passado > 15 and tempo_atual - tempo_ultima_bomba > intervalo_bomba:
            if random.randint(1, 100) <= 10:
                bombas.add(Bomba(assets, velocidade=velocidade_padrao, direcao=random.choice(direcoes)))
                tempo_ultima_bomba = tempo_atual


        frutas.update()
        bombas.update()
        particulas.update()
        explosoes.update()

        # Verifica frutas que passaram da tela
        for fruta in frutas.copy():
            if not fruta.cortada and fruta.tipo == 'normal' and (fruta.rect.top > HEIGHT or fruta.rect.right < 0 or fruta.rect.left > WIDTH):
                frutas.remove(fruta)
                fruta.kill()
                vidas -= 1
                if vidas >= 0:
                    vida_estado[vidas] = False
                    animacao_coracao(screen, assets, vidas)
                if vidas <= 0:
                    pygame.mixer.music.stop()
                    fade_out(screen)
                    return pontos
                

        #colisões -  mouse (faca) com a fruta
        if pygame.mouse.get_pressed()[0]:  #detecta movimento mouse
            mouse_pos = pygame.mouse.get_pos()
            for fruta in frutas:
                if fruta.rect.collidepoint(mouse_pos):
                    # Aplica efeitos como se fosse a faca
                    if fruta.tipo == 'dourada':
                        pontos += 20
                        modo_bonus = True
                        bonus_timer = pygame.time.get_ticks()
                        assets['bonus_sound'].play()
                    elif fruta.tipo == 'congelada':
                        congelado = True
                        congelado_timer = pygame.time.get_ticks()
                        FPS_padrao = 30
                        pontos += 5 * (2 if modo_bonus else 1)
                        assets['bonus_sound'].play()
                    elif fruta.tipo == 'vida':
                        if vidas < 3:
                            vidas += 1
                            vida_estado[vidas - 1] = True
                            assets['life_sound'].play()
                    elif fruta.tipo == 'explosiva':
                        assets['explosiva_explode'].play()
                        for f in frutas.copy():
                            pontos += 5
                            f.kill()
                            particulas.add(Particula(f.rect.centerx, f.rect.centery, (255, 100, 0)))
                        shake_screen(screen)
                    else:
                        pontos += 5 * (2 if modo_bonus else 1)
                        assets['faca_sound'].play()

                    fruta.cortada = True
                    fruta.kill()

                    # Partículas
                    for _ in range(10):
                        particulas.add(Particula(fruta.rect.centerx, fruta.rect.centery, (255, 255, 0)))

                
        for bomba in bombas.copy():
            if pygame.mouse.get_pressed()[0] and bomba.rect.collidepoint(mouse_pos):
                bomba.kill()
                assets['explosion_sound'].play()
                pygame.mixer.music.stop()

                shake_screen(screen)
                fade_out(screen)
                return pontos

        
        screen.blit(imagem_fundo, (0,0))


        #efeitos de congelamento
        if congelado:
            if pygame.time.get_ticks() - congelado_timer > duracao_congelado:
                congelado = False
                FPS_padrao = 60

        if modo_bonus:
            tempo = (pygame.time.get_ticks() - bonus_timer) / 1000
            if tempo > 10:
                modo_bonus = False
                FPS_padrao = 60
                pygame.mixer.music.load(assets['musica_normal'])
                pygame.mixer.music.play(-1)

        screen.blit(fundo_atual, (0,0))

        #desenha os sprites na tela
        frutas.draw(screen)
        particulas.draw(screen)
        bombas.draw(screen)
        facas.draw(screen)

        if congelado:
            filtro = pygame.Surface((WIDTH, HEIGHT))
            filtro.fill((100, 180, 255))  # azul claro
            filtro.set_alpha(100)         # transparência
            screen.blit(filtro, (0, 0))
        #faca acompanha o mouse
        mouse = pygame.mouse.get_pos()
        screen.blit(assets['faca'], (mouse[0] - FACA_WIDTH // 2, mouse[1] - FACA_HEIGHT // 2))

        #pontos na tela
        texto_str = f"Pontos: {pontos}"
        #defina a cor do texto principal
        cor_texto = YELLOW if modo_bonus else WHITE
        texto_base, bordas = render_text_com_borda(fonte, texto_str, cor_texto)
        #desenha as bordas primeiro
        for dx, dy, borda_img in bordas:
            screen.blit(borda_img, (10 + dx, 10 + dy))
        #desenha o texto principal por cima
        screen.blit(texto_base, (10, 10))


        #desenha as vidas na tela - corações
        for i in range(3):
            x = 10 + i * 35
            y = 50
            if vida_estado[i]:
                screen.blit(assets['vida cheia'], (x, y))
            else:
                screen.blit(assets['vida vazia'], (x, y))
        
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


#Shake effect (ajuda do Copilot)
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


# Função para renderizar texto com borda (ajuda de inteligencia artificial)
def render_text_com_borda(fonte, texto, cor_texto, cor_borda=BLACK):
    #texto original
    texto_base = fonte.render(texto, True, cor_texto)
    texto_borda = []

    #cria 8 posições ao redor para a borda
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                texto_borda.append((dx, dy, fonte.render(texto, True, cor_borda)))

    return texto_base, texto_borda