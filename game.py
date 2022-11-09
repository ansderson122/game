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
    level.run()
    
    
    pygame.display.update()
    relogio.tick(60)
    