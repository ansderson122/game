import pygame 


class inimigo1:
    def __init__(self,surface):
        self.surface = surface
        self.imagem = pygame.image.load('graphics/Inimigos/l1.png').convert_alpha()
        self.rect = self.imagem.get_rect(bottomright = (600,300))
        self.tempo = 0

        self.velocidade = 5
                
    def mover(self):
        self.rect.x -= 1 * self.velocidade
        if self.rect.x <= -100: self.rect.x = 800

    def alteraVelocidade(self,tempo):
        if tempo%5 == 0 and tempo != 0:
            self.velocidade+=(1/60)

    def animacao(self):
        self.tempo +=1
        if self.tempo <= (60/self.velocidade):
            self.imagem = pygame.image.load('graphics/Inimigos/l1.png').convert_alpha()
        elif self.tempo <= (2*60/self.velocidade):
            self.imagem = pygame.image.load('graphics/Inimigos/l2.png').convert_alpha()
        elif self.tempo <= (3*60/self.velocidade):
            self.imagem = pygame.image.load('graphics/Inimigos/l3.png').convert_alpha()
        elif self.tempo <= (4*60/self.velocidade):
            self.imagem = pygame.image.load('graphics/Inimigos/l4.png').convert_alpha()
        elif self.tempo <= (5*60/self.velocidade):
            self.imagem = pygame.image.load('graphics/Inimigos/l5.png').convert_alpha()
        else:
            self.tempo = 0

    def update(self):
        self.mover()
        self.animacao()
        self.surface.blit(self.imagem, self.rect)