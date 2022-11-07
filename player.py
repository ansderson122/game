import pygame

class player():
    def __init__(self,surface):
        self.surface = surface
        self.imagem = pygame.image.load('graphics/Player/player_walk_1.png')
        self.rect = self.imagem.get_rect(midbottom = (80,300))
        self.player_gravidade = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.gravidade()                     
       

        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.player_gravidade = -20

        if keys[pygame.MOUSEBUTTONDOWN] and self.rect.bottom >= 300:
            self.player_gravidade = -20

    def gravidade(self):
       
        self.player_gravidade += 1 

    def update(self):
        self.get_input()
        self.rect.y += self.player_gravidade
        if self.rect.bottom >= 300: self.rect.bottom = 300
        self.surface.blit(self.imagem, self.rect)     