import pygame
from config import *

pygame.init()

def init_screen(screen):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(IMG_DIR, 'fundo.jpeg')).convert()
    background_rect = background.get_rect()

    botoes = {
        "Fácil": pygame.Rect(300, 250, 200, 50),
        "Médio": pygame.Rect(300, 320, 200, 50),
        "Difícil": pygame.Rect(300, 390, 200, 50)
    }

    font = pygame.font.SysFont('Arial', 40)

    game_on = True
    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                game_on = False


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
        screen.blit(background, background_rect)

        for dificuldade, rect in botoes.items():
            pygame.draw.rect(screen, (0, 0, 0), rect)  # Cor branca para os botões
            texto_render = font.render(dificuldade, True, BLACK)
            screen.blit(texto_render,(rect.x + (rect.width - texto_render.get_width()) // 2, rect.y + (rect.height - texto_render.get_height()) // 2))

        pygame.display.flip()

    return state