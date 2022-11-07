import pygame

class menu():
    def __init__(self,surface):
        self.fonte = pygame.font.Font(None, 25)
        self.surface = surface
        self.active = True

        self.areaMenu = pygame.Surface((250,250))
        self.areaMenu.fill('grey')
        self.rect = self.areaMenu.get_rect(topleft = (275,100))

        

    def botaoInicia(self):
        self.inicia = pygame.Surface((150,50))
        self.inicia.fill('white')
        self.iniciaRect = self.inicia.get_rect(topleft = (325,150))

        score_surf = self.fonte.render('Inicia o jogo', False, (0,0,0))
        score_rect = score_surf.get_rect(topleft = (350,170))
        
        
        self.surface.blit(self.inicia,self.iniciaRect)
        self.surface.blit(score_surf, score_rect)

    def draw(self):
        self.surface.blit(self.areaMenu,self.rect)
        self.botaoInicia()