import pygame
from config import *
from assets import *
from classes import *
from init_screen import *
from game import *


def game_over_screen(screen, pontos, assets):
    clock = pygame.time.Clock()
    font = assets['gameover_font']
    font_pontuacao = assets['padrao_font']

    background = pygame.image.load(os.path.join(IMG_DIR, 'fundo.jpg')).convert()

    #criação do botão de jogar Novamente
    botao_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 100, 400, 50)

    game_over = True

    while game_over:
        clock.tick(FPS)
        
        #verifica se o jogador quer jogar novamente ou sair do jogo
        #sair do jogo se não quiser mais jogar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT

            #jogo reinicia 
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if botao_rect.collidepoint(event.pos):
                    return ON

        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        #Texto de Game Over
        texto_gameover = font.render("GAME OVER", True, WHITE)
        screen.blit(texto_gameover, (WIDTH // 2 - texto_gameover.get_width() // 2, HEIGHT // 2 - 150))

        #Pontuação
        texto_pontuacao = font_pontuacao.render(f"Pontuação: {pontos}", True, WHITE)
        screen.blit(texto_pontuacao, (WIDTH // 2 - texto_pontuacao.get_width() // 2, HEIGHT // 2-50))

        #Botão jogar novamente
        pygame.draw.rect(screen, WHITE, botao_rect)
        texto_jogar = font_pontuacao.render("Jogar Novamente", True, BLACK)
        screen.blit(texto_jogar, (botao_rect.x + (botao_rect.width - texto_jogar.get_width()) // 2, botao_rect.y + (botao_rect.height - texto_jogar.get_height()) // 2))

        pygame.display.flip()
