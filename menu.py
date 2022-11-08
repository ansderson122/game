import pygame

class menu():
    def __init__(self,surface):
        self.fonte = pygame.font.Font(None, 25)
        self.surface = surface
        self.active = True 
        self.selecaoDificudade = False

        

    def botaoInicia(self):
        self.inicia = pygame.Surface((150,50))
        self.inicia.fill('white')
        self.iniciaRect = self.inicia.get_rect(topleft = (325,150))

        score_surf = self.fonte.render('Inicia o jogo', False, (0,0,0))
        score_rect = score_surf.get_rect(topleft = (350,170))
        
        
        self.surface.blit(self.inicia,self.iniciaRect)
        self.surface.blit(score_surf, score_rect)

    def clickInicia(self):
        self.mouse = pygame.mouse.get_pos() 
        event = pygame.event.wait()

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] :
            if  (self.mouse[0] >= 350 and self.mouse[0] <= 475) and (self.mouse[1] >= 150 and self.mouse[1] <= 200):
                self.selecaoDificudade = True


    def draw(self):
        self.clickInicia()
        if not self.selecaoDificudade:
            self.botaoInicia()
        else:
            pass