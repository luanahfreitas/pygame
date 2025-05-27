import pygame
from assets import *
from config import *
from assets import load_assets

pygame.init()

def init_screen(screen,assets):
    #tempo de jogo iniciado
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(IMG_DIR, 'fundo.jpg')).convert()  #carregando imagem de fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  #ajustando iamgem de fundo as configurações da tela

    font_titulo = assets['titulo_font'] #carregando fonte do titulo
    font = assets['padrao_font'] #carregando fonte dos botões

    #definindo os estados de acordo com o botão clicado
    botoes = {
        "Fácil": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50),
        "Médio": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - (-10), 200, 50),
        "Difícil": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - (-70), 200, 50)
    }

    #inicializando o estado do jogo
    game_on = True
    while game_on:
        clock.tick(FPS)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #verifica se o jogador quer sair do jogo
                state = QUIT
                game_on = False


            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #verifica se o jogador clicou com o botão esquerdo do mouse
                for dificuldade, rect in botoes.items():
                    #clique no botão
                    if rect.collidepoint(event.pos):
                        if dificuldade == "Fácil":
                            state = EASY
                        elif dificuldade == "Médio":
                            state = MEDIUM
                        elif dificuldade == "Difícil":
                            state = HARD
                        game_on = False
            
        screen.fill(BLACK)
        screen.blit(background, (0,0))

        #configurando o titulo
        titulo_text = font_titulo.render("desFRUTANDO", True, BLACK)  #fonte do titulo
        titulo_rect = titulo_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))  #centralizando o titulo na tela
        screen.blit(titulo_text, titulo_rect)

        #ajuste dos botões
        for dificuldade, rect in botoes.items():
            mouse_pos = pygame.mouse.get_pos()  #posição do mouse
            #desenho do botão
            if rect.collidepoint(mouse_pos):  #clique do mouse sobre o botão
                #Hover: borda azul, fundo cinza claro
                pygame.draw.rect(screen, BLACK, rect, width=3)  #borda
                inner_rect = rect.inflate(-6, -6)
                pygame.draw.rect(screen, (200, 200, 200), inner_rect)  #fundo hover
            else:
                #normal: borda preta, fundo branco
                pygame.draw.rect(screen, BLACK, rect, width=3)  #borda
                inner_rect = rect.inflate(-6, -6)
                pygame.draw.rect(screen, WHITE, inner_rect)  #fundo normal


            #texto
            texto = font.render(dificuldade, True, BLACK)
            texto_rect = texto.get_rect(center=rect.center)
            screen.blit(texto, texto_rect)

        pygame.display.flip()

    return state