import pygame
from assets import load_assets
from config import *
import random
from classes import Fruta, Bomba, Particula


def tela_jogo(screen,dificuldade,assets):
    clock = pygame.time.Clock()  #tempo do jogo
    tempo_inicio = pygame.time.get_ticks()  #marca o tempo de início do jogo

    vidas = 3  #quantidade de vidas inicial do jogador
    vida_estado = [True,True,True]  #estado das vidas, True = vida cheia, False = vida vazia

    fonte = assets['padrao_font']

    #cria os grupos de sprites
    facas = pygame.sprite.Group()
    bombas = pygame.sprite.Group()
    frutas = pygame.sprite.Group()
    particulas = pygame.sprite.Group()
    explosoes = pygame.sprite.Group()

    #carrega as imagens das frutas e dos fundos de acordo com a dificuldade
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

    #carrega a imagem de fundo
    fundo_atual = imagem_fundo

    #pontos e estado do jogo inicial
    pontos = 0
    state = ON

    #musica de fundo
    pygame.mixer.music.load(assets['musica_normal'])  #carrega a musica de fundo
    pygame.mixer.music.play(-1)  # loop infinito da musica
    pygame.mixer.music.set_volume(0.4)  #volume da musica

    #modo de congelamento
    congelado = False  #inicializa o congelamento como False
    congelado_timer = 0  #marca o tempo de congelamento
    duracao_congelado = 5000  #duração do congelamento em milissegundos (5 segundos)
    
    #modo bônus
    modo_bonus = False  #inicializa o modo bônus como False
    bonus_timer = 0 #marca o tempo do bônus

    FPS_padrao = 60  #FPS padrão do jogo

    #controladores de tempo
    tempo_ultima_fruta = pygame.time.get_ticks()  # marca o tempo da última fruta gerada
    intervalo_fruta = 1200  # 1 fruta a cada 1.2 segundos

    tempo_ultima_bomba = pygame.time.get_ticks()  # marca o tempo da última bomba gerada
    intervalo_bomba = 4000  # bomba só pode cair a cada 4 segundos

    

    while state != DONE:
        clock.tick(FPS_padrao)  #controla a taxa de quadros do jogo
        tempo_atual = pygame.time.get_ticks()  #marca o tempo atual do jogo
        tempo_passado = (tempo_atual - tempo_inicio) / 1000  #tempo passado em segundos

        direcoes = ['baixo']  #direção inicial das frutas 
        velocidade_padrao = 3 + pontos // 30  #velocidade das frutas aumenta com os pontos

        # verifica se o jogador atingiu 150 pontos para mudar a direção e o fundo
        if pontos >= 150:
            direcoes = ['baixo', 'esquerda', 'direita']  #direções adicionais para as frutas
            fundo_atual = fundo_extremo  #muda o fundo para o modo extremo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #verifica se o jogador quer sair do jogo
                return pontos
                
        

        #frutas com intervalo de tempo
        if tempo_atual - tempo_ultima_fruta > intervalo_fruta:
            r = random.randint(1, 135)  #gera um número aleatório entre 1 e 135
            #cria a fruta de acordo o número aleatório
            if pontos >= 80:  #frutas especiais aparecem depois de 80 pontos
                if r <= 20:  # 20% de chance de ser uma fruta dourada
                    frutas.add(Fruta(assets['dourada'], tipo='dourada', velocidade=velocidade_padrao, direcao=random.choice(direcoes),))
                elif r <= 50:  # 30% de chance de ser uma fruta congelada
                    frutas.add(Fruta(assets['gelo'], tipo='congelada', velocidade=velocidade_padrao, direcao=random.choice(direcoes)))
                else:  # 50% de chance de ser uma fruta normal
                    frutas.add(Fruta(imagem_fruta, tipo='normal', velocidade=velocidade_padrao, direcao=random.choice(direcoes)))

            else:  #antes de 80 pontos só caem frutas normais
                frutas.add(Fruta(imagem_fruta, tipo='normal', velocidade=velocidade_padrao, direcao=random.choice(direcoes)))
            tempo_ultima_fruta = tempo_atual



        #bombas - só depois de 15s
        if tempo_passado > 15 and tempo_atual - tempo_ultima_bomba > intervalo_bomba:  #verifica se já passou 15 segundos do inicio do jogo e se o intervalo de bomba foi atingido
            if random.randint(1, 100) <= 10:  # 10% de chance de cair uma bomba
                bombas.add(Bomba(assets, velocidade=velocidade_padrao, direcao=random.choice(direcoes)))
                tempo_ultima_bomba = tempo_atual

        # Atualiza os grupos de sprites
        frutas.update()
        bombas.update()
        particulas.update()
        explosoes.update()

        #vidas (ajuda do Copilot)
        #verifica frutas que passaram da tela sem serem cortadas
        for fruta in frutas.copy():  #usa copy() para evitar problemas de modificação do conjunto durante a iteração
            if not fruta.cortada and fruta.tipo == 'normal' and (fruta.rect.top > HEIGHT or fruta.rect.right < 0 or fruta.rect.left > WIDTH):  #verifica se a fruta não foi cortada e se saiu dos limites da tela
                frutas.remove(fruta)  #remove a fruta do grupo
                fruta.kill()  #remove a fruta da tela
                vidas -= 1  #diminui a quantidade de vidas
                if vidas >= 0:  #verifica se ainda há vidas restantes
                    vida_estado[vidas] = False  #atualiza o estado da vida
                    animacao_coracao(screen, assets, vidas)  #animação do coração
                if vidas <= 0:  #verifica se não há mais vidas - game over
                    pygame.mixer.music.stop()  #para a música de fundo
                    fade_out(screen)  #efeito de fade out na tela
                    return pontos  #retorna a pontuação final
                

        #colisões -  mouse (faca) com a fruta
        if pygame.mouse.get_pressed()[0]:  #detecta movimento mouse
            mouse_pos = pygame.mouse.get_pos()  #pega a posição do mouse
            for fruta in frutas:  #verifica cada fruta no grupo de frutas
                if fruta.rect.collidepoint(mouse_pos):  #verifica se a fruta foi cortada (colisão com o mouse/faca)
                    #aplica efeitos como se fosse a faca
                    if fruta.tipo == 'dourada':  #fruta dourada
                        pontos += 15  #adiciona 20 pontos
                        modo_bonus = True  #ativa o modo bônus
                        bonus_timer = pygame.time.get_ticks()  #marca o tempo do bônus
                        assets['bonus_sound'].play()  #toca o som do bônus
                    elif fruta.tipo == 'congelada':  #fruta congelada
                        congelado = True  #ativa o congelamento
                        congelado_timer = pygame.time.get_ticks()   #marca o tempo do congelamento
                        FPS_padrao = 30  #reduz o FPS para 30 FPS
                        pontos += 5 * (2 if modo_bonus else 1)  #adiciona os pontos (5 ou 10 se estiver no modo bônus)
                        assets['freeze_sound'].play()  #toca o som de congelamento
                    else:  #fruta normal
                        pontos += 5 * (2 if modo_bonus else 1)  #adiciona os pontos (5 ou 10 se estiver no modo bônus)
                        assets['faca_sound'].play()  #toca o som da faca

                    fruta.cortada = True  #marca a fruta como cortada
                    fruta.kill()  #remove a fruta da tela

                    #partículas de fruta cortada
                    for _ in range(10): #cria 10 partículas
                        particulas.add(Particula(fruta.rect.centerx, fruta.rect.centery, (255, 255, 0)))  #partículas amarelas para frutas normais e bonus
                        if fruta.tipo == 'congelada':
                            particulas.add(Particula(fruta.rect.centerx, fruta.rect.centery, (100, 180, 255)))
        
        #colisões - mouse (faca) com a bomba
        #acaba com o jogo se a bomba for cortada
        for bomba in bombas.copy():  # verifica cada bomba no grupo de bombas
            if pygame.mouse.get_pressed()[0] and bomba.rect.collidepoint(mouse_pos):  #verifica se a bomba foi cortada (colisão com o mouse/faca)
                bomba.kill()  #remove a bomba da tela
                assets['explosion_sound'].play()  #toca o som da explosão
                pygame.mixer.music.stop()  #para a música de fundo

                shake_screen(screen)  #efeito de tremer na tela
                fade_out(screen)  #efeito de fade out na tela
                return pontos  #retorna a pontuação final

        
        screen.blit(imagem_fundo, (0,0))


        #efeitos de congelamento
        if congelado:  #verifica se o jogo está congelado
            if pygame.time.get_ticks() - congelado_timer > duracao_congelado:  #verifica se o tempo de congelamento acabou
                congelado = False  #desativa o congelamento
                FPS_padrao = 60  #volta o FPS para 60

        #efeitos de bônus
        if modo_bonus:  #verifica se o modo bônus está ativo
            tempo = (pygame.time.get_ticks() - bonus_timer) / 1000  #tempo em segundos desde que o bônus foi ativado
            if tempo > 10:  #verifica se o tempo do bônus acabou
                modo_bonus = False  #desativa o modo bônus
                FPS_padrao = 60  #volta o FPS para 60

        screen.blit(fundo_atual, (0,0))

        #desenha os sprites na tela
        frutas.draw(screen)
        particulas.draw(screen)
        bombas.draw(screen)
        facas.draw(screen)

        if congelado:  #se o jogo estiver congelado, desenha um filtro azul
            filtro = pygame.Surface((WIDTH, HEIGHT))  #cria uma superfície para o filtro (do tamanho da tela)
            filtro.fill((100, 180, 255))  # azul claro
            filtro.set_alpha(100)         # transparência
            screen.blit(filtro, (0, 0))
        
        #faca acompanha o mouse
        mouse = pygame.mouse.get_pos()
        screen.blit(assets['faca'], (mouse[0] - FACA_WIDTH // 2, mouse[1] - FACA_HEIGHT // 2))


        #coloca os pontos na tela
        texto_str = f"Pontos: {pontos}"  #pontos na tela
        cor_texto = YELLOW if modo_bonus else WHITE   #defina a cor do texto principal (amarelo se estiver no modo bônus, branco se estiver normal)
        texto_base, bordas = render_text_com_borda(fonte, texto_str, cor_texto)  #renderiza texto com borda

        #desenha as bordas primeiro
        for dx, dy, borda_img in bordas:
            screen.blit(borda_img, (10 + dx, 10 + dy))
        #desenha o texto principal por cima
        screen.blit(texto_base, (10, 10))


        #desenha as vidas na tela - corações
        for i in range(3):
            x = 10 + i * 35  #posição x dos corações
            y = 50  #posição y dos corações
            if vida_estado[i]:  #verifica se a vida está cheia
                screen.blit(assets['vida cheia'], (x, y))  #desenha coração cheio
            else:  
                screen.blit(assets['vida vazia'], (x, y))  #desenha coração vazio
        
        pygame.display.flip()  #atualiza a tela
        

#fade out efeito
def fade_out(screen, velocidade=10):
    fade = pygame.Surface((WIDTH, HEIGHT))  #cria uma superfície do tamanho da tela
    fade.fill((0, 0, 0))  #preenche a superfície com preto

    #Loop para aumentar a opacidade do fade
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
        #cria uma cópia da imagem com opacidade reduzido
        img = cheio.copy()
        img.set_alpha(alpha)

        screen.blit(vazio, (x, y))    
        screen.blit(img, (x, y))
        pygame.display.flip()
        pygame.time.delay(30)


# Função para renderizar texto com borda (feito por inteligencia artificial)
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