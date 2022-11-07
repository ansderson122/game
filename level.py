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

        self.caracol = caracol(self.surface)
        self.player = player(self.surface)

    def display_score(self):
        timer = int((pygame.time.get_ticks())/1000 - self.tempoInicial)
        score_surf = self.fonte.render(f'{timer}', False, (0,0,0))
        score_rect = score_surf.get_rect(center = (400,50))
        self.surface.blit(score_surf, score_rect)


    def setup_level(self):
        self.surface.blit(self.ceu,(0,0))
        self.surface.blit(self.terra,(0,300))
        #tela.blit(text_surface, (600, 40))
        self.caracol.update()
        self.display_score()
        self.caracol.mover()
      
        #tela.blit(player_surface, player_rect)

        
        if self.caracol.rect.colliderect(self.player.rect):
            game_active = False

    def run(self):
        self.setup_level()