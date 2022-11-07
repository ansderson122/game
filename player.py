import pygame

class player():
    def __init__(self):
        self.imagem = pygame.image.load('graphics/Player/player_walk_1.png')
        self.rect = self.imagem.get_rect(midbottom = (80,300))
        self.gravidade = 0

    def get_input(self):
        keys = pygame.key.get_pressed()                     
       
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravidade = -20
            