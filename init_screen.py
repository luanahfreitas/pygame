import pygame
from assets import *
from config import *
from assets import load_assets

pygame.init()

def init_screen(screen,assets):
    #tempo de jogo iniciado
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(IMG_DIR, 'fundo.jpeg')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  #ajustando iamgem de fundo as configurações da tela

    font_titulo = assets['titulo_font']
    font = assets['padrao_font']

    # Definindo os estados de acordo com o botão clicado
    botoes = {
        "Fácil": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50),
        "Médio": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - (-10), 200, 50),
        "Difícil": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - (-70), 200, 50)
    }

    game_on = True
    while game_on:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                game_on = False


            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
        titulo_text = font_titulo.render("desFRUTANDO", True, WHITE)
        titulo_rect = titulo_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(titulo_text, titulo_rect)

        #ajuste dos botões
        for dificuldade, rect in botoes.items():
            pygame.draw.rect(screen,WHITE,rect)    # Cor branca para os botões
            texto = font.render(dificuldade, True, BLACK)
            texto_rect = texto.get_rect(center=rect.center)
            screen.blit(texto, texto_rect)

        pygame.display.flip()

    return state