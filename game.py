import pygame
from sys import exit
from level import level

pygame.init()
tela = pygame.display.set_mode((800,400))
pygame.display.set_caption('Meu Joquin')
relogio = pygame.time.Clock()

level = level(tela)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not level.game_active:    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                level.game_active = True
                level.caracol.rect.left = 800
                tempoInicial = int((pygame.time.get_ticks())/1000)
    if level.game_active:
        level.run()
    
    
    pygame.display.update()
    relogio.tick(60)
    