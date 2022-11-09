import pygame 


class caracol():
    def __init__(self,surface):
        self.surface = surface
        self.imagem = pygame.image.load('graphics/Inimigos/snail1.png').convert_alpha()
        self.rect = self.imagem.get_rect(bottomright = (600,300))

        self.velocidade = int()
        
    def mover(self):
        self.rect.x -= 1 * self.velocidade
        if self.rect.x <= -100: self.rect.x = 800

    def alteraVelocidade(self,tempo):
        if tempo%5 == 0 and tempo != 0:
            self.velocidade+=(1/60)


    def update(self):
        self.mover()
        self.surface.blit(self.imagem, self.rect)