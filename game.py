import pygame
from sys import exit
from level import level

pygame.init()
tela = pygame.display.set_mode((800,400))
pygame.display.set_caption('Meu Joquin')
relogio = pygame.time.Clock()


game_active = True

level = level(tela)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_active:    
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                caracol1_rect.left = 800
                tempoInicial = int((pygame.time.get_ticks())/1000)
            #if event.type == pygame.KEYUP:
            #   if event.type == pygame.K_SPACE and player_rect >= 300:
            #       player_gravidade = -20
    if game_active:

        level.run()
        
        #player
        
        #player_gravidade += 1
        #player_rect.y += player_gravidade
        #if player_rect.bottom >= 300: player_rect.bottom = 300
        
        #if player_rect.colliderect(caracol1_rect):
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
        #    print('colidiu')
        
   
    #else:
    
    pygame.display.update()
    relogio.tick(60)
    