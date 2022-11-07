import pygame
from sys import exit

def display_score():
    timer = int((pygame.time.get_ticks())/1000 - tempoInicial)
    score_surf = fonte.render(f'{timer}', False, (0,0,0))
    score_rect = score_surf.get_rect(center = (400,50))
    tela.blit(score_surf, score_rect)

pygame.init()
tela = pygame.display.set_mode((800,400))
pygame.display.set_caption('Meu Joquin')
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 50)

game_active = True

tempoInicial = 0

ceu_surface = pygame.image.load('graphics/Tela/Sky.png').convert()
terra_surface = pygame.image.load('graphics/Tela/ground.png').convert()
#text_surface = fonte.render('meu joguin',True,(0,0,0))

inimigo_caracol = pygame.image.load('graphics/Inimigos/snail1.png').convert_alpha()
caracol1_rect = inimigo_caracol.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png')
player_rect = player_surface.get_rect(midbottom = (80,300))

player_gravidade = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                player_gravidade = -20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                        player_gravidade = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                caracol1_rect.left = 800
                tempoInicial = int((pygame.time.get_ticks())/1000)
            #if event.type == pygame.KEYUP:
            #   if event.type == pygame.K_SPACE and player_rect >= 300:
            #       player_gravidade = -20
    if game_active:

        tela.blit(ceu_surface,(0,0))
        tela.blit(terra_surface,(0,300))
        #tela.blit(text_surface, (600, 40))
        tela.blit(inimigo_caracol, caracol1_rect)
        display_score()
        caracol1_rect.x -= 5
        if caracol1_rect.x <= -100: caracol1_rect.x = 800
        tela.blit(player_surface, player_rect)
        
        #player
        
        player_gravidade += 1
        player_rect.y += player_gravidade
        if player_rect.bottom >= 300: player_rect.bottom = 300
        
        #if player_rect.colliderect(caracol1_rect):
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
        #    print('colidiu')
        
        if caracol1_rect.colliderect(player_rect):
            game_active = False
    #else:
    
    pygame.display.update()
    relogio.tick(60)
    