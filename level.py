import pygame 
from inimigo import caracol
from player import player

class level():
    def __init__(self, surface):
        self.surface = surface
        self.ceu =  pygame.image.load('graphics/Tela/Sky.png').convert()
        self.terra = pygame.image.load('graphics/Tela/ground.png').convert()

        self.tempoInicial = 0
        self.fonte = pygame.font.Font(None, 50)
        self.game_active = True

        self.caracol = caracol(self.surface)
        self.player = player(self.surface)

    def display_score(self):
        timer = int((pygame.time.get_ticks())/1000 - self.tempoInicial)
        score_surf = self.fonte.render(f'{timer}', False, (0,0,0))
        score_rect = score_surf.get_rect(center = (400,50))
        self.surface.blit(score_surf, score_rect)

    def colliderect1(self):
        if self.caracol.rect.colliderect(self.player.rect):
            self.game_active = False


    def setup_level(self):
        self.surface.blit(self.ceu,(0,0))
        self.surface.blit(self.terra,(0,300))
        
    def run(self):
        self.setup_level()

        

        self.caracol.update()
        self.display_score()
       
        self.player.update()
        
        self.colliderect1()