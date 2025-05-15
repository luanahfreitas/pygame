import pygame
from assets import *
from config import *

pygame.init()

def init_screen(screen,assets):
    clock = pygame.time.Clock()
    assets = load_assets()

    background = pygame.image.load(path.join(IMG_DIR, 'fundo.jpeg')).convert()

    botoes = {
        "Fácil": pygame.Rect(300, 250, 200, 50),
        "Médio": pygame.Rect(300, 320, 200, 50),
        "Difícil": pygame.Rect(300, 390, 200, 50)
    }
    
    font = assets['padrao_font']

    game_on = True
    while game_on:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                game_on = False


            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for dificuldade, rect in botoes.items():
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

        for dificuldade, rect in botoes.items():
            pygame.draw.rect(screen,WHITE,rect)    # Cor branca para os botões
            texto = font.render(dificuldade, True, BLACK)
            screen.blit(texto,(rect.x + (rect.width - texto.get_width()) // 2, rect.y + (rect.height - texto.get_height()) // 2))

        pygame.display.flip()

    return state