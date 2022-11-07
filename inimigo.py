import pygame 


class caracol():
    def __init__(self,surface):
        self.surface = surface
        self.imagem = pygame.image.load('graphics/Inimigos/snail1.png').convert_alpha()
        self.rect = self.imagem.get_rect(bottomright = (600,300))

        self.velocidade = 5
        
    def mover(self):
        self.rect.x -= 1 * self.velocidade
        if self.rect.x <= -100: self.rect.x = 800   

    def update(self):
        self.surface.blit(self.imagem, self.rect)